from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    #빈 사전 만들어주기
    word_dictionary={} #<단어>:몇번, <단어>:몇번 쌍으로 넣어있음
    for word in words: #word는 반복문 변수, words는 리스트
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add word to word_dictionary
            word_dictionary[word]=1 #이걸 result.html에 넣어줘야하지

    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary': word_dictionary.items()})
