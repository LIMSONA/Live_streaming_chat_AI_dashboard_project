# 뷰 : 기능을 담당(페이지 단위) / 화면이 나타나는 뷰, 화면이 없는 뷰. 화면이 있건없건 url은 필수
# 함수형뷰 , 클래스형뷰, 제네릭뷰


from django.http import HttpResponse

def index(request): 
    #데이터베이스 조회, 수정, 등록
    #응답메세지를 만들어서 반환
    #나중에 html 변수를 대신해서 템플릿 사용
    #함수형 뷰는 매게변수로 꼭 request로 써야함. 추가가능
    html = "<html><body>Hi Django.</body></html>"
    

# 뷰 이름 : LiveCommerce
# 뷰 접속 주소 : LiveCommerce/
# 내용 : hello LiveCommerce_test mode
def LiveCommerce(request): 
    html = "<html><body>hello LiveCommerce_test mode</body><html>"
    return HttpResponse(html)


def template_test(request):
    return render(request, 'test.html')