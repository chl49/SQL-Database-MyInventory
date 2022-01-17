### Example inspired by Tutorial at https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
### However the actual example uses sqlalchemy which uses Object Relational Mapper, which are not covered in this course. I have instead used natural sQL queries for this demo. 

from flask import Flask, render_template, url_for, flash, redirect
from forms import AddForm, ClientForm, OrderForm, AssignOrderForm, DeleteForm, DeleteClientForm, DeleteCourierForm, DeleteOrderForm, UpdateForm, UpdateOrdersForm, EditOrderForm, EditAssignOrderForm, EditCourierForm, ViewForm

import mysql.connector

#change this into your own credentials
host = "localhost"
user = "root"
password = "llVll*88"
database = "myinventory"

mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=password,
  database=database
)

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts2 = []
print("Hello World")
mycursor = mydb.cursor()
"""
mycursor.execute("SELECT * FROM client")
#posts2 = mycursor.fetchall()


for y in mycursor:
    print(y)
    posts2.append(y)
print(mydb)
for hey in posts2:
    print(hey[1])
print("Hello World")

posts = []
posts=posts2
mycursor = mydb.cursor()

mycursor2 = mydb2.cursor()

mycursor2.execute("SELECT * FROM Orders")

for x in mycursor2:
    print(x)
    posts.append(x)

#print(mydb)
print("follow me")
"""

"""

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
"""

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
@app.route("/")
@app.route("/home")
def home():
    #return render_template('home.html', posts=posts)
    return render_template('home.html')

"""
@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html', title='Register')
"""

@app.route("/viewtables", methods=['GET', 'POST'])
def viewtables():
    form = ViewForm()

    choices = ['Client', 'Orders', 'Courier', 'AssignOrder', 'Products', 'Location', 'Seller', 'ThirdPartySeller', 'ThirdPartyItemsSold']
    form.ViewType.choices = choices

    if form.validate_on_submit():
        if form.ViewType.data == 'Client':
            return redirect(url_for('client'))

        elif form.ViewType.data == 'Orders':
            return redirect(url_for('orders'))
        
        elif form.ViewType.data == 'Courier':
            return redirect(url_for('courier'))
        
        elif form.ViewType.data == 'AssignOrder':
            return redirect(url_for('assignorders'))
        
        elif form.ViewType.data == 'Products':
            return redirect(url_for('products'))
        
        elif form.ViewType.data == 'Location':
            return redirect(url_for('location'))
        
        elif form.ViewType.data == 'Seller':
            return redirect(url_for('seller'))
        
        elif form.ViewType.data == 'ThirdPartySeller':
            return redirect(url_for('thirdpartyseller'))

        else:
            return redirect(url_for('thirdpartyitemssold'))

    return render_template('viewtables.html', title='View Tables', form=form)

@app.route("/client")
def client():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    conn.row_factory = dict_factory
    
    c = conn.cursor()
    
    c.execute("SELECT * FROM client")
    posts = c.fetchall()
    
    return render_template('client.html', posts=posts)

@app.route("/orders")
def orders():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    conn.row_factory = dict_factory
    
    c = conn.cursor()
    
    c.execute("SELECT * FROM orders")
    posts = c.fetchall()
    
    return render_template('orders.html', posts=posts)

@app.route("/assignorders")
def assignorders():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    conn.row_factory = dict_factory
    
    c = conn.cursor()
    
    c.execute("SELECT * FROM assignOrder")
    posts = c.fetchall()
    
    return render_template('assignorders.html', posts=posts)

@app.route("/courier")
def courier():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    conn.row_factory = dict_factory
    
    c = conn.cursor()
    
    c.execute("SELECT * FROM courier")
    posts = c.fetchall()
    
    return render_template('courier.html', posts=posts)

@app.route("/products", methods=['GET', 'POST'])
def products():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    conn.row_factory = dict_factory
    
    c = conn.cursor()
    
    c.execute("SELECT * FROM products")
    posts = c.fetchall()
    
    return render_template('products.html', posts=posts)

@app.route("/location", methods=['GET', 'POST'])
def location():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    conn.row_factory = dict_factory
    
    c = conn.cursor()
    
    c.execute("SELECT * FROM location")
    posts = c.fetchall()
    
    return render_template('location.html', posts=posts)

@app.route("/seller", methods=['GET', 'POST'])
def seller():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    conn.row_factory = dict_factory
    
    c = conn.cursor()
    
    c.execute("SELECT * FROM seller")
    posts = c.fetchall()
    
    return render_template('seller.html', posts=posts)

@app.route("/thirdpartyseller", methods=['GET', 'POST'])
def thirdpartyseller():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    conn.row_factory = dict_factory
    
    c = conn.cursor()
    
    c.execute("SELECT * FROM thirdpartyseller")
    posts = c.fetchall()
    
    return render_template('thirdpartyseller.html', posts=posts)

@app.route("/thirdpartyitemssold", methods=['GET', 'POST'])
def thirdpartyitemssold():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    conn.row_factory = dict_factory
    
    c = conn.cursor()
    
    c.execute("SELECT * FROM thirdpartyitemssold")
    posts = c.fetchall()
    
    return render_template('thirdpartyitemssold.html', posts=posts)

@app.route("/joins")
def joins():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    conn.row_factory = dict_factory
    
    c = conn.cursor()
    c.execute("SELECT client.clientName, orders.orderID FROM client JOIN orders on client.ClientID = orders.CLientID")
    posts = c.fetchall()
    
    return render_template('joins.html', posts=posts)

@app.route("/divides")
def divides():
    """
    conn = sqlite3.connect('blog.db')

    #Display all blogs from the 'blogs' table
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM blogs")
    posts = c.fetchall()
    """
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    conn.row_factory = dict_factory
    
    c = conn.cursor()
    #c.execute("SELECT * FROM client AS c WHERE NOT EXISTS ((SELECT * FROM orders) EXCEPT(SELECT * FROM orders AS o WHERE o.ClientID = c.ClientID) )")
    #c.execute("SELECT ClientID FROM client AS c WHERE NOT EXISTS (SELECT * FROM orders AS o WHERE o.ClientID = c.ClientID)")
    #c.execute("SELECT DISTINCT c1.ClientID AS ClientID FROM client AS c1 WHERE NOT EXISTS (SELECT o.ClientID FROM orders AS o WHERE o.ClientID = c1.ClientID)")
    #c.execute("SELECT DISTINCT o1.OrderID AS OrderID FROM orders o1 WHERE NOT EXISTS (SELECT * FROM assignorder ao WHERE NOT EXISTS (SELECT * from products p WHERE p.OrderID=o1.OrderID AND ao.OrderID=o1.OrderID))")
    c.execute("SELECT DISTINCT c1.CourierID AS CourierID FROM AssignOrder c1 WHERE NOT EXISTS (SELECT * FROM orders o WHERE NOT EXISTS (SELECT * from AssignOrder c2 WHERE c2.CourierID=c1.CourierID AND c2.OrderID=o.OrderID))")
    posts = c.fetchall()
    
    return render_template('divides.html', posts=posts)

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()

    choices = ['Client', 'Orders', 'AssignOrder']
    form.AddType.choices = choices

    if form.validate_on_submit():
        if form.AddType.data == 'Client':
            return redirect(url_for('add_client'))

        elif form.AddType.data == 'Orders':
            return redirect(url_for('add_orders'))

        else:
            return redirect(url_for('add_assignorder'))

    return render_template('add.html', title='Update', form=form)

@app.route("/add_client", methods=['GET', 'POST'])
def add_client():
    print("registerpage")
    form = ClientForm()

    if form.validate_on_submit():
        #conn = sqlite3.connect('blog.db')
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        c = conn.cursor()
        print("registerquery")
        #Add the new blog into the 'blogs' table
        query = 'insert into client VALUES (%s, %s, %s, %s, %s)'
        #c.execute(query, (form.username.data, form.email.data, form.password.data)) #Execute the query
        c.execute(query, (form.ClientID.data, form.ClientName.data, form.ClientAddress.data, form.Phone.data, form.Email.data)) #Execute the query
        conn.commit() #Commit the changes
        flash(f'Account created for {form.ClientName.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('add_client.html', title='Add Client', form=form)


@app.route("/add_orders", methods=['GET', 'POST'])
def add_orders():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    #conn.row_factory = lambda cursor, row: row[0]
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT ClientID FROM client")
    results = c.fetchall()
    clients=[]
    boolean=[True,False]
    clients = [(results.index(item), item[0]) for item in results]
    #users = [(item[0]) for item in results]
    form = OrderForm()
    form.ClientID.choices = clients
    form.IsPremium.choices = boolean
    
    #form.username.choices = [(item) for item in users]

    if form.validate_on_submit():
        clientChoices = form.ClientID.choices
        #ClientID =  (clientChoices[form.ClientID.data][1])
        ClientID=(clientChoices[int(form.ClientID.data)][1])
        print("client choices")
        #print(form.ClientID.data)
        #user =  (choices[form.username.data][1])
        OrderID = form.OrderID.data
        EstimatedArrivalDate = form.EstimatedArrivalDate.data
        DateOrderReceived = form.DateOrderReceived.data
        Quantity=form.Quantity.data
        premiumChoices = form.IsPremium.choices
        #IsPremium=(premiumChoices[form.IsPremium.data])
        #IsPremium=(premiumChoices[(form.IsPremium.data)][1])
        if(form.IsPremium.data==True):
            premium='TRUE'
            IsPremium=True;
        else:
            premium='FALSE'
            IsPremium=False;
            
        DeliveryAddress=form.DeliveryAddress.data
        ShippingCost=form.ShippingCost.data
        #Add the new blog into the 'blogs' table in the database
        query = 'insert into orders (OrderID, EstimatedArrivalDate, DateOrderReceived, Quantity, IsPremium, DeliveryAddress, ShippingCost, ClientID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)' #Build the query
        c.execute(query, (OrderID, EstimatedArrivalDate, DateOrderReceived, Quantity, IsPremium, DeliveryAddress, ShippingCost, ClientID)) #Execute the query
        conn.commit() #Commit the changes

        flash(f'Order queue created for {ClientID}!', 'success')
        return redirect(url_for('home'))
    
    return render_template('add_orders.html', title='Add Order', form=form)


@app.route("/add_assignorder", methods=['GET', 'POST'])
def add_assignorder():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    #conn.row_factory = lambda cursor, row: row[0]
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM client")
    clients = c.fetchall()
    id_to_name = {}
    for client in clients:
        id_to_name[client[0]] = client[1]

    c.execute("SELECT * FROM orders")
    posts = c.fetchall()
    order_options = {}
    for post in posts:
        option = post[0] + '(' + id_to_name[post[7]] + ')'
        order_options[option] = post[0]

    c.execute("SELECT * FROM courier")
    posts = c.fetchall()
    courier_options = {}
    for post in posts:
        option = post[0] + '(' + post[1] + ')'
        courier_options[option] = post[0]

    form = EditAssignOrderForm()
    form.OrderID.choices = list(order_options.keys())
    form.CourierID.choices = list(courier_options.keys())

    if form.validate_on_submit():
        order = order_options[form.OrderID.data]
        courier = courier_options[form.CourierID.data]

        query = "insert into assignorder (OrderID,CourierID) VALUES ('" + str(order) +"','" + str(courier) +"');"
        print(query)
        c.execute(query)
        conn.commit()
        flash(f'Successfully added record', 'success')
    #form.username.choices = [(item) for item in users]
    
    return render_template('add_assignorder.html', title='Add AssignOrder', form=form)


'''
MY CODE STARTS HERE
'''

#Delete page
@app.route("/delete", methods=['GET', 'POST'])
def delete():
    form = DeleteForm()

    choices = ['Client', 'Courier', 'Orders']
    form.DeleteType.choices = choices

    if form.validate_on_submit():
        if form.DeleteType.data == 'Client':
            return redirect(url_for('delete_client'))

        elif form.DeleteType.data == 'Courier':
            return redirect(url_for('delete_courier'))

        else:
            return redirect(url_for('delete_order'))

    return render_template('delete.html', title='Delete', form=form)

@app.route("/delete_client", methods=["GET", "POST"])
def delete_client():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    c = conn.cursor()
    c.execute("SELECT * FROM client")
    posts = c.fetchall()
    options = {}
    for post in posts:
        option = post[0] + '(' + post[1] + ')'
        options[option] = post[0]

    form = DeleteClientForm()
    form.ClientID.choices = list(options.keys())

    if form.validate_on_submit():
        choice = form.ClientID.data
        client_id = options[choice]
        query = "DELETE FROM client WHERE ClientId='" + str(client_id) + "';"
        c.execute(query)

        conn.commit()  # Commit the changes
        flash(f'Client {choice} deleted with cascade!', 'success')
        return redirect(url_for("home"))

    return render_template('delete_client.html', title='Delete Client', form=form)

@app.route("/delete_courier", methods=['GET', 'POST'])
def delete_courier():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    c = conn.cursor()
    c.execute("SELECT * FROM courier")
    posts = c.fetchall()
    options = {}
    for post in posts:
        option = post[0] + '(' + post[1] + ')'
        options[option] = post[0]

    form = DeleteCourierForm()
    form.CourierID.choices = list(options.keys())

    if form.validate_on_submit():
        choice = form.CourierID.data
        courier_id = options[choice]
        query = "DELETE FROM courier WHERE CourierId='" + str(courier_id) + "';"
        c.execute(query)

        conn.commit()  # Commit the changes
        flash(f'Courier {choice} deleted with cascade!', 'success')
        return redirect(url_for("home"))

    return render_template('delete_courier.html', title='Delete Courier', form=form)

@app.route("/delete_order", methods=['GET', 'POST'])
def delete_order():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    c = conn.cursor()
    c.execute("SELECT * FROM client")
    clients = c.fetchall()
    id_to_name = {}
    for client in clients:
        id_to_name[client[0]] = client[1]

    c.execute("SELECT * FROM orders")
    posts = c.fetchall()
    options = {}
    for post in posts:
        option = post[0] + '(' + id_to_name[post[7]] + ')'
        options[option] = post[0]

    form = DeleteOrderForm()
    form.OrderID.choices = list(options.keys())

    if form.validate_on_submit():
        choice = form.OrderID.data
        order_id = options[choice]
        query = "DELETE FROM orders WHERE OrderId='" + str(order_id) + "';"
        c.execute(query)

        conn.commit()  # Commit the changes
        flash(f'Order {choice} deleted with cascade!', 'success')
        return redirect(url_for("delete_order"))

    return render_template('delete_order.html', title='Delete Order', form=form)

@app.route("/update", methods=['GET', 'POST'])
def update():
    form = UpdateForm()

    choices = ['Orders', 'AssignOrder', 'Courier']
    form.UpdateType.choices = choices

    if form.validate_on_submit():
        if form.UpdateType.data == 'Orders':
            return redirect(url_for('update_orders'))

        elif form.UpdateType.data == 'AssignOrder':
            return redirect(url_for('update_assignorder'))

        else:
            return redirect(url_for('update_courier'))

    return render_template('update.html', title='Update', form=form)

@app.route("/update_orders", methods=['GET', 'POST'])
def update_orders():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    c = conn.cursor()
    c.execute("SELECT * FROM client")
    clients = c.fetchall()
    id_to_name = {}
    for client in clients:
        id_to_name[client[0]] = client[1]

    c.execute("SELECT * FROM orders")
    posts = c.fetchall()
    options = {}
    for post in posts:
        option = post[0] + '(' + id_to_name[post[7]] + ')'
        options[option] = post[0]

    form = UpdateOrdersForm()
    form.OrderID.choices = list(options.keys())

    if form.validate_on_submit():
            return redirect(url_for('edit_order', orderID=options[form.OrderID.data]))


    return render_template('update_orders.html', title='Update Orders', form=form)

@app.route("/update_assignorder", methods=['GET', 'POST'])
def update_assignorder():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    c = conn.cursor()
    c.execute("SELECT * FROM client")
    clients = c.fetchall()
    id_to_name = {}
    for client in clients:
        id_to_name[client[0]] = client[1]

    c.execute("SELECT * FROM orders")
    posts = c.fetchall()
    order_options = {}
    for post in posts:
        option = post[0] + '(' + id_to_name[post[7]] + ')'
        order_options[option] = post[0]

    c.execute("SELECT * FROM courier")
    posts = c.fetchall()
    courier_options = {}
    for post in posts:
        option = post[0] + '(' + post[1] + ')'
        courier_options[option] = post[0]

    form = EditAssignOrderForm()
    form.OrderID.choices = list(order_options.keys())
    form.CourierID.choices = list(courier_options.keys())

    if form.validate_on_submit():
        order = order_options[form.OrderID.data]
        courier = courier_options[form.CourierID.data]

        query = "UPDATE assignorder SET CourierID='" + str(courier) +"' WHERE OrderID='" + str(order) +"';"
        print(query)
        c.execute(query)
        conn.commit()

        flash(f'Successfully updated record', 'success')

    return render_template('update_assignorder.html', title='Update AssignOrders', form=form)

@app.route("/update_courier", methods=['GET', 'POST'])
def update_courier():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    c = conn.cursor()
    c.execute("SELECT * FROM courier")
    posts = c.fetchall()
    options = {}
    for post in posts:
        option = post[0] + '(' + post[1] + ')'
        options[option] = post[0]

    form = EditCourierForm()
    form.CourierID.choices = list(options.keys())

    if form.validate_on_submit():
        courier = options[form.CourierID.data]
        lat = form.TrackingLocationLat.data
        lng = form.TrackingLocationLng.data

        query = "UPDATE courier SET TrackingLocationLat=" + str(lat) + " WHERE CourierID='" + str(courier) +"';"
        c.execute(query)

        query = "UPDATE courier SET TrackingLocationLng=" + str(lng) + " WHERE CourierID='" + str(courier) + "';"
        c.execute(query)

        conn.commit()

        flash(f'Successfully updated record', 'success')

    return render_template('update_courier.html', title='Update Courier', form=form)

@app.route("/update_orders/<orderID>", methods=['GET', 'POST'])
def edit_order(orderID):
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    c = conn.cursor()
    c.execute('SELECT * FROM orders')
    posts = c.fetchall()

    form = EditOrderForm()

    choices = ["No Change", "TRUE", "FALSE"]
    form.IsPremium.choices = choices


    if form.validate_on_submit():
        if form.EstimatedArrivalDate.data != None:
            date = form.EstimatedArrivalDate.data
            query = "UPDATE orders SET EstimatedArrivalDate='" + str(date) + "' WHERE OrderID='" + str(orderID) + "';"
            c.execute(query)
            conn.commit()

        if form.Quantity.data != None:
            quantity = form.Quantity.data
            query = "UPDATE orders SET Quantity=" + str(quantity) + " WHERE OrderID='" + str(orderID) + "';"
            c.execute(query)
            conn.commit()

        if form.IsPremium.data != 'No Change':
            isPremium = form.IsPremium.data
            query = "UPDATE orders SET IsPremium=" + str(isPremium) + " WHERE OrderID='" + str(orderID) + "';"
            c.execute(query)
            conn.commit()

        if form.DeliveryAddress.data != None and form.DeliveryAddress.data != '':
            address = form.DeliveryAddress.data
            query = "UPDATE orders SET DeliveryAddress='" + str(address) + "' WHERE OrderID='" + str(orderID) + "';"
            c.execute(query)
            conn.commit()

        if form.ShippingCost.data != None:
            shippingCost = form.ShippingCost.data
            query = "UPDATE orders SET ShippingCost=" + str(shippingCost) + " WHERE OrderID='" + str(orderID) + "';"
            c.execute(query)
            conn.commit()

        flash(f'Successfully updated record', 'success')

    return render_template('edit_order.html', title='Edit Order', form=form)

@app.route("/orderInfo", methods=['GET', 'POST'])
def orderInfo():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    c = conn.cursor()
    options = {}
    query ="SELECT COUNT(*) FROM orders;"
    c.execute(query)
    totalOrders=c.fetchall()
    query = "SELECT OrderID, Quantity FROM orders WHERE Quantity=(SELECT MAX(Quantity) FROM orders);"
    c.execute(query)
    maxQuantitiy=c.fetchall();
    query = "SELECT OrderID, Quantity FROM orders WHERE Quantity=(SELECT MIN(Quantity) FROM orders);"
    c.execute(query)
    minQuantitiy=c.fetchall();
    print("max quantity is: \n")
    print(maxQuantitiy[0][0])
    orderData=[totalOrders,maxQuantitiy,minQuantitiy]
    #return redirect(url_for('delete_client'))
    return render_template('orderInfo.html', title='Order Stats', orderData=orderData)

@app.route("/shippingInfo", methods=['GET', 'POST'])
def shippingInfo():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    c = conn.cursor()
    options = {}
    query ="SELECT COUNT(*) FROM orders;"
    c.execute(query)
    totalOrders=c.fetchall()
    query = "SELECT ShippingCost, COUNT(*) FROM Orders GROUP BY ShippingCost ORDER BY Count(*) ASC LIMIT 1;"
    c.execute(query)
    maxCharge=c.fetchall();
    query = "SELECT ShippingCost, COUNT(*) FROM Orders GROUP BY ShippingCost ORDER BY Count(*) DESC LIMIT 1;"
    c.execute(query)
    minCharge=c.fetchall();
    print("max shipping charge is: \n")
    print(maxCharge[0][0])
    shipData=[totalOrders, maxCharge, minCharge]
    #return redirect(url_for('delete_client'))
    return render_template('shippingInfo.html', title='Order Shipment Stats', orderData=shipData)


if __name__ == '__main__':
    app.run(debug=True)


