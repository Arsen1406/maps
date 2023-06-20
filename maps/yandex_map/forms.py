from django import forms


class Coordinates(forms.Form):
    coordinate_x = forms.DecimalField(label='Долгота: ', required=True)
    coordinate_y = forms.DecimalField(label='Широта: ', required=True)
    zoom = forms.FloatField(
        max_value=21,
        min_value=2,
        label='Увеличение: ',
        required=True
    )
