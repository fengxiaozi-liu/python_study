from django import forms
from rbac import models
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from rbac.forms.base import BaseForm


class RoleForm(forms.ModelForm):
    """
    角色验证的Form表单
    """

    class Meta:
        model = models.Role
        fields = ['title', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }


class UserForm(forms.ModelForm):
    """
        用户验证的Form表单
    """
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = models.UserInfo
        fields = ['name', 'email', 'password', 'confirm_password']
        """
        设置样式的方式之一，还可以采用重写的方法，设置样式
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
        两种方式设置错误提示，这种方法是自己设置
        还有一种方式，就是在配置中，将语言编程中文
        error_messages = {
            'name': {'required': '用户名不能为空'},
            'password': {'required': '密码不能为空'},
            'email': {'required': '邮箱不能为空'},
            'confirm_password': {'required': '确认密码不能为空'},
        }
        """

    # 统一添加样式
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'
            if name == 'confirm_password':
                filed.widget.attrs['type'] = 'password'

    def clean_confirm_password(self):
        """
        钩子函数
        用来检测密码是否一致
        :return:
        """
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('两次密码输入不一致')
        return confirm_password


class UpdateUserForm(forms.ModelForm):
    """
    更新用户的Form表单
    """

    class Meta:
        model = models.UserInfo
        fields = ['name', 'email']


class ResetPwdForm(forms.ModelForm):
    """
    重置密码的Form表单
    """
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = models.UserInfo
        fields = ['password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(ResetPwdForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('两次密码输入不一次')
        return confirm_password


class MenuForm(forms.ModelForm):
    """
    一级菜单的form表单验证
    """

    class Meta:
        icon_list = [
            ('fa fa-telegram', mark_safe('<i class="fa fa-telegram" aria-hidden="true"></i>')),
            ('fa fa-circle-o', mark_safe('<i class="fa fa-circle-o" aria-hidden="true"></i>')),
            ('fa fa-coffee', mark_safe('<i class="fa fa-coffee" aria-hidden="true"></i>')),
            ('fa fa-car', mark_safe('<i class="fa fa-car" aria-hidden="true"></i>')),
            ('fa fa-cloud-upload', mark_safe('<i class="fa fa-cloud-upload" aria-hidden="true"></i>')),
            ('fa fa-envelope-o', mark_safe('<i class="fa fa-envelope-o" aria-hidden="true"></i>')),
            ('fa fa-info-circle', mark_safe('<i class="fa fa-info-circle" aria-hidden="true"></i>')),
            ('fa fa-magnet', mark_safe('<i class="fa fa-magnet" aria-hidden="true"></i>')),
            ('fa fa-plane', mark_safe('<i class="fa fa-plane" aria-hidden="true"></i>')),
            ('fa fa-sign-in', mark_safe('<i class="fa fa-sign-in" aria-hidden="true"></i>')),
            ('fa fa-tags', mark_safe('<i class="fa fa-tags" aria-hidden="true"></i>')),
            ('fa fa-graduation-cap', mark_safe('<i class="fa fa-graduation-cap" aria-hidden="true"></i>')),
        ]
        model = models.Menu
        fields = ['title', 'icon']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.RadioSelect(choices=icon_list, attrs={'class': 'clearfix'})
        }


class SecondMenuForm(BaseForm):
    class Meta:
        model = models.Permission
        exclude = ['pid']


class ThirdMenuForm(forms.ModelForm):
    class Meta:
        model = models.Permission
        fields = ['title', 'name', 'url']

    def __init__(self, *args, **kwargs):
        super(ThirdMenuForm, self).__init__(*args, **kwargs)
        for name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'
        # 采用选择框的时候要重写choices
        # self.fields['pid'].choices = models.Permission.objects.filter(menu_id__isnull=False).values_list('id', 'title')


class MultiAddPermissionForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    menu_id = forms.ChoiceField(
        choices=[(None, '------')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    pid_id = forms.ChoiceField(
        choices=[(None, '------')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(MultiAddPermissionForm, self).__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += models.Permission.objects.filter(pid_id__isnull=True).exclude(
            menu__isnull=True).values_list('id', 'title')


class MultiUpdatePermissionForm(forms.Form):
    id = forms.IntegerField(
        widget=forms.HiddenInput(),
    )
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    menu_id = forms.ChoiceField(
        choices=[(None, '------')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    pid_id = forms.ChoiceField(
        choices=[(None, '------')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(MultiUpdatePermissionForm, self).__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += models.Permission.objects.filter(pid_id__isnull=True).exclude(
            menu__isnull=True).values_list('id', 'title')
