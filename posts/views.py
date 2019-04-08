from django.shortcuts import render, redirect
from .forms import Postform

# Create your views here.

def list(request):
    return render(request, 'posts/list.html')
    
def create(request):
    #1.get 방식으로 데이터를 입력할 form을 요청한다.
    #4.사용자는 데이터를 입력해서 post방식으로 요청을 보낸다.
    #9. 사용자가 다시 적절한 데이터를 입력해서 post방식으로 요청한다.
    
    if request.method =='POST':
        #5. post방식으로 저장요청을 받고 데이터를 받아 PostForm에 넣어서 인스턴스화 한다.
        #10. 5번과 동일하다
        form = PostForm(request.POST)
        #6.데이터 검증을 한다.
        #11. 6번과 동일하다.
        if form.is_valid():
            #12. 적절한 데이터가 들어온다. 데이터를 저장하고 list 페이지로 리다이렉트
            form.save()
            return redirect('posts:list')
        else:
            #7.적절하지 않은 데이터가 들어온다
            print
            pass
    else:
    #2. Postform을 인스턴스화 시켜서 form이라는 변수에 저장한다.
        form = Postform()
        #3. form을 담아서 create.html을 보내준다.
        #8. 사용자가 입력한 데이터가  form에 담아진 상태로 다시 form을 담아서  create.html을 보내준다.
        
    return render(request, 'posts/create.html', {'form':form})
    




