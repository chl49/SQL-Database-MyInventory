from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, NumberRange
from wtforms.fields.html5 import IntegerField, DecimalField


class ClientForm(FlaskForm):
	ClientID = StringField('ClientID',validators=[DataRequired()])
	ClientName = StringField('ClientName', validators=[DataRequired()])
	ClientAddress = StringField('ClientAddress', validators=[DataRequired()])
	Phone = StringField('Phone', validators=[DataRequired()])
	Email = StringField('Email',validators=[DataRequired(), Email()])
	submit = SubmitField('Sign Up')


class OrderForm(FlaskForm):
    OrderID = StringField('OrderID', validators=[DataRequired()])
    EstimatedArrivalDate = StringField('EstimatedArrivalDate', validators=[DataRequired()])
    DateOrderReceived = StringField('DateOrderReceived', validators=[DataRequired()])
    Quantity = IntegerField('Quantity', validators=[Optional(),NumberRange(min=0)])
    IsPremium = SelectField('IsPremium', choices=[])
    DeliveryAddress = StringField('DeliveryAddress', validators=[Optional()])
    ShippingCost = IntegerField('ShippingCost', validators=[Optional(),NumberRange(min=0)])
    ClientID = SelectField('ClientID', choices=[])
    submit = SubmitField('Submit')
    
class AssignOrderForm(FlaskForm):
    OrderID = SelectField('OrderID', choices=[])
    CourierID = SelectField('CourierID', choices=[])
    submit = SubmitField('Submit')
    
class AddForm(FlaskForm):
    AddType = SelectField('Entry', choices=[])
    submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
    DeleteType = SelectField('Table', choices=[])
    submit = SubmitField('Submit')

class DeleteClientForm(FlaskForm):
    ClientID = SelectField("ID", choices=[])
    submit = SubmitField('Delete')

class DeleteCourierForm(FlaskForm):
    CourierID = SelectField("ID", choices=[])
    submit = SubmitField('Delete')

class DeleteOrderForm(FlaskForm):
    OrderID = SelectField("ID", choices=[])
    submit = SubmitField('Delete')

class UpdateForm(FlaskForm):
    UpdateType = SelectField("Field")
    submit = SubmitField('Submit')

class UpdateOrdersForm(FlaskForm):
    OrderID = SelectField('Choose order to update', choices=[])
    submit = SubmitField('Edit')

class EditOrderForm(FlaskForm):
    EstimatedArrivalDate = DateField('Estimated Arrival Date(yyyy-mm-dd)', validators=[Optional()])
    Quantity = IntegerField('Quantity', validators=[Optional(), NumberRange(min=0)])
    IsPremium = SelectField('Premium Status', choices=[])
    DeliveryAddress = StringField('Delivery Address', validators=[Optional()])
    ShippingCost = DecimalField('Shipping Cost', validators=[Optional(), NumberRange(min=0)])
    submit = SubmitField('Update')

class EditAssignOrderForm(FlaskForm):
    OrderID = SelectField('Choose order to assign courier', choices=[])
    CourierID = SelectField('Courier', choices=[])
    submit = SubmitField('Assign')

class EditCourierForm(FlaskForm):
    CourierID = SelectField('Select Courier', choices=[])
    TrackingLocationLat = DecimalField('Enter Latitude', validators=[DataRequired()])
    TrackingLocationLng = DecimalField('Enter Longitude', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class ViewForm(FlaskForm):
    ViewType = SelectField('Views', choices=[])
    submit = SubmitField('Submit')
