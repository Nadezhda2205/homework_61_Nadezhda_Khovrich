from django.views.generic import TemplateView
from accounts.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


class LoginView(TemplateView):
    template_name = 'account/login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('login')
        print(user.get_username())
        print(user.is_authenticated)
        login(request,user)
        return redirect('task_list')
        
def logout_view(request):
    logout(request)
    return redirect('task_list')


