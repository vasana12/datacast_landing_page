from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.
from django.contrib.auth import get_user_model
from landing.models import Boards
from landing.models import Review_product
from landing.models import Review_search_task
from landing.models import BoardCategories
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import BoardsCreateForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.http import Http404
from landing.models import Boards_keyword_number
import json
import pandas as pd
from landing.engine.crawl import navershopping_list
from landing.engine.data_util import dao
from landing.models import Datacast_request
from .forms import Review_search_task, Review_product


def fix_element(str):
    ##to fix_element string to json
    global str_to_df, num_count_df
    str_before_fixed = str.replace('{', '').replace('}', '')
    str_to_dict = {i.split(': ')[0]: i.split(': ')[1] for i in str_before_fixed.split(', ')}
    for key, value in str_to_dict.items():
        str_to_dict[key] = int(value)
        num_count_df = pd.DataFrame()

    num_count_df['keyword'] = str_to_dict.keys()
    num_count_df['count'] = str_to_dict.values()
    num_count_df_records = num_count_df.to_dict(orient='records')
    return num_count_df_records

class BoardDetailView(DetailView):
    model = Boards

    def get_queryset(self):
        #user는 객체이므로, user 밑에 email과 비교를 원한다면 user__email 사용
        print('hello')
        print(self.request.user)
        user = get_object_or_404(get_user_model(),username__exact=self.request.user)
        queryset_input = Boards.objects.filter(id=self.kwargs.get('pk'),user_id=user.id)

        return queryset_input


    def get_context_data(self, **kwargs):
        user = get_object_or_404(get_user_model(), username__exact=self.request.user)
        context = super(BoardDetailView, self).get_context_data(**kwargs)
        board_keyword_number = Boards_keyword_number.objects.get(boards_id=self.kwargs.get('pk'))
        num_count_df_recordsA = fix_element(board_keyword_number.A_top300)
        num_count_df_recordsB = fix_element(board_keyword_number.B_top300)
        num_count_df_recordsAB = fix_element(board_keyword_number.AB_top300)
        num_count_list = zip(num_count_df_recordsA, num_count_df_recordsB, num_count_df_recordsAB)
        context = {
            'num_count_list': num_count_list
        }
        context['board'] = Boards.objects.get(id=self.kwargs.get('pk'), user_id=user.id)

        return context
    # def dispatch(self, request, *args, **kwargs):

class BoardListView(LoginRequiredMixin,ListView):
    template_name = 'landing/boards_list.html'
    model = Boards

    def get_queryset(self, **kwargs):
        #user는 객체이므로, user 밑에 email과 비교를 원한다면 user__email 사용
        print('hello')
        print(self.request.user)
        user = get_object_or_404(get_user_model(),username__exact=self.request.user)
        queryset = Boards.objects.filter(user=user)
        print(queryset)
        return queryset


# class Datacast_requestCreateView(LoginRequiredMixin,CreateView):
#     model = Datacast_request
#     print('hello_datacast_request')
#     template_name = 'landing/review_search_task_form.html'
#     form_class = Datacast_request
#     fields = ['product']
#     # print(fields)
#     success_url = reverse_lazy('landing:datacast_request_add')
#
#     def form_valid(self, form):
#         print('form:',form)
#         # messages.success(self.request, mark_safe("키워드 설정이 완료 되었습니다."
#         #                                          "<button class='IBMPlexSansKR-Text bold' onclick=location.href='/boards_list/'>결과보기</button>"))
#         super().form_valid(form)
#         return HttpResponseRedirect(self.get_success_url())

class Review_search_taskCreateView(LoginRequiredMixin,CreateView):
    info_sended = False
    search_keyword = ''
    template_name = 'landing/review_search_task_form.html'
    model = Review_search_task
    fields = ['user','search_keyword']
    success_url = reverse_lazy('landing:review_search_task_add')
    task_id= ''
    is_searched = 0
    def form_valid(self, form):
        self.info_sended = True
        self.is_searched = 1
        #Instead of return this HttpResponseRedirect, return an new rendered page
        # messages.success(self.request, mark_safe("키워드 설정이 완료 되었습니다. <span style='color:#bd2130';>분석 대상 제품을 선택해 주세요</span>"))
        super(Review_search_taskCreateView, self).form_valid(form)
        search_keyword = self.object.search_keyword
        self.search_keyword =search_keyword
        task_id = navershopping_list.get_navershopping_product_list(search_keyword,self.object.id)
        self.task_id = task_id
        return render(self.request, self.template_name, self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super(Review_search_taskCreateView,self).get_context_data(**kwargs)
        ctx['info_sended'] = self.info_sended
        if ctx['info_sended'] == True:
            product_list = Review_product.objects.filter(review_search_task__exact=self.task_id)
            ctx['is_searched'] = self.is_searched
            ctx['product_list'] = product_list
        return ctx
    # return HttpResponseRedirect(self.get_success_url())

        # product_list = Review_product.objects.filter(search_keyword__contains=search_keyword)
    #     ctx['object_list'] = product_list
    #
    #     return ctx
class BoardCreateView(LoginRequiredMixin,CreateView):
        model = Boards
        fields = ['user','keywordA','keywordB','periodStartA','periodEndA','periodStartB','periodEndB','channel','analysis_type']
        print(fields)
        success_url = reverse_lazy('landing:analysis_add')
        def form_valid(self, form):
            messages.success(self.request,mark_safe("키워드 설정이 완료 되었습니다."
                                                    "<button class='IBMPlexSansKR-Text bold' onclick=location.href='/boards_list/'>결과보기</button>"))
            super().form_valid(form)
            return HttpResponseRedirect(self.get_success_url())
        #
        # def form_invalid(self, form):
        #     return super().form_invalid(form)
def datacast_request_create(request):
    # ajax로 요청했는지 확인하기 위해, is_ajax가 true 인지 확인
    is_ajax = request.POST.get('is_ajax')
    review_request = Datacast_request.objects.all()
    # boards = Boards.objects.all()
    datacast_request = Datacast_request.objects.create()
    print('--------------------------')
    if is_ajax:
        print('--------------------------')
        print('is_ajax:',is_ajax)
        obj_str_list = request.POST.getlist('obj_dict_list[]')
        user = request.user
        datacast_request.user = user
        datacast_request.channel = 'review'
        obj_dict_list = [json.loads(obj_str) for obj_str in obj_str_list]
        print(obj_dict_list)
        # datacast_request.product = [int(obj_dict['productID']) for obj_dict in obj_dict_list]
        # datacast_request.product_row_table_id = [int(obj_dict['review_product_table_id']) for obj_dict in obj_dict_list]
        datacast_request.save()

        ##datacast request to batch
        dao.request_batch(datacast_request, 'navershopping')
        ##ajax 를 통해 선택된 객체가 1개 이상일 때

        # 데이터를 요청한 페이지에 {'works':True}라는 json 데이터 전달
        return JsonResponse({'works':True})

# def boards_result(request):
#     print('board_result')
#     return render(request,'landing/boards_result.html')

def main_page(request):
    return render(request,'landing/index.html')

def start(request):
    return render(request,'landing/start.html')


def almaden_datahero(request):
    return render(request,'landing/almaden_datahero.html')

def index(request):
    return render(request,'landing/index.html')

def blog(request):
    return render(request,'landing/blog.html')

def test(request):
    return render(request, 'landing/boards_list.html')

# def feature(request):
#     return render(request,'landing/feature.html')

def pricing(request):
    return render(request,'landing/pricing.html')


def contact(request):
    return render(request,'landing/contact.html')

def blog_details(request):
    return render(request,'landing/blog-details.html')

def login(request):
    return render(request,'landing/login.html')