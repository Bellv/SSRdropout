from django import forms

from .models import Member

class AddMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'name',
            'description',
            'gb_name',
            'gb_id',
            'gb_character',
            'gb_waifu',
            'facebook',
            'twitter',
            'discord'
        ]

    def __init__(self, *args, **kwargs):
        super(AddMemberForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'input'
        self.fields['name'].label = 'Name *'

        self.fields['description'].widget.attrs['class'] = 'input'
        self.fields['description'].label = 'Description'

        self.fields['gb_name'].widget.attrs['class'] = 'input'
        self.fields['gb_name'].label = 'Granblue Fantasy Name'

        self.fields['gb_character'].widget.attrs['class'] = 'input'
        self.fields['gb_character'].label = 'Main Character'

        self.fields['gb_id'].widget.attrs['class'] = 'input'
        self.fields['gb_id'].label = 'Granblue Fantasy ID'

        self.fields['gb_waifu'].widget.attrs['class'] = 'input'
        self.fields['gb_waifu'].label = 'Waifu'

        self.fields['facebook'].widget.attrs['class'] = 'input'
        self.fields['facebook'].label = 'Facebook'

        self.fields['twitter'].widget.attrs['class'] = 'input'
        self.fields['twitter'].label = 'Twitter'

        self.fields['discord'].widget.attrs['class'] = 'input'
        self.fields['discord'].label = 'Discord'

class InactiveMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'name',
            'status',
        ]

    def __init__(self, *args, **kwargs):
        super(InactiveMemberForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['class'] = 'input'
        self.fields['status'].label = 'Status'
