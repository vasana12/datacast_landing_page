from landing.models import Datacast_batch, Datacast_request_batch

def request_batch(datacast_request, channel):
    ##product_id_list 를 1개씩 분리해서 관리
    # datacast_request.product to datacast_batch.product
    # review 는 post_data null 로 처리 ex)navershopping

    datacast_request_id = datacast_request.id


    product_id_list = datacast_request.product
    fromdate = datacast_request.fromdate
    todate = datacast_request.todate

    if (fromdate==None and todate==None):
        print('review')
    else:
        print('blog or new')
    #   기간이 있는 경우 batch 를 월단위로 잘라서 진행한다.

    # print(datacast_request_id, product_id_list)
    # Datacast_batch.objects.filter(product=)
    # select * from datacast_batch where product and post_date and keyword

    # for product_id in product_id_list:
    #     print(product_id)
    #     datacast_batch = Datacast_batch.objects.create(channel=channel,product=product_id)
    #     datacast_batch.save()

    # Datacast_request_batch.objects.ge()
    # product_id_list = product_id_list.replace('[','')
    # product_id_list = product_id_list.replace(']', '')
    # print(product_id_list)
