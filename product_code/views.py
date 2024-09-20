from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import requests
from django.http import JsonResponse
from django.views import View


class HomePage(TemplateView):
    template_name = 'home.html'


class SendProductName(View):
    template_name = 'sendname.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def get_package_code(self, product_name):
        try:
            search_url = f"https://tasnif.soliq.uz/api/cls-api/mxik/search-subposition?search_text={product_name}&page=0&size=15&lang=ru"
            search_response = requests.get(search_url)
            search_data = search_response.json()

            if not search_data.get('content') or 'mxikCode' not in search_data['content'][0]:
                return None, 'Продукт не найден'

            mxik_code = search_data['content'][0]['mxikCode']

            package_url = f"https://tasnif.soliq.uz/api/cls-api/mxik/get/by-mxik?mxikCode={mxik_code}&lang=ru"
            package_response = requests.get(package_url)
            package_data = package_response.json()

            if not package_data.get('packages') or 'packageCode' not in package_data['packages'][0]:
                return mxik_code, 'Код упаковки не найден'

            package_code = package_data['packages'][0]['packageCode']

            return mxik_code, package_code

        except Exception as e:
            return None, f'Произошла ошибка: {str(e)}'

    def post(self, request, *args, **kwargs):
        product_name = request.POST.get('product_name')

        if not product_name:
            return JsonResponse({'error': 'Название продукта не указано'})

        mxik_code, result = self.get_package_code(product_name)

        if mxik_code and isinstance(result, str):
            return JsonResponse({'mxikCode': mxik_code, 'error': result})
        elif mxik_code:
            return JsonResponse({'mxikCode': mxik_code, 'packageCode': result})
        else:
            return JsonResponse({'error': result})
