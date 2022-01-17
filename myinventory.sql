CREATE SCHEMA `myinventory`;

USE MYINVENTORY;

CREATE TABLE Client (
    ClientID CHAR(9) NOT NULL,
    ClientName VARCHAR(50),
    ClientAddress VARCHAR(80) NOT NULL,
    Phone CHAR(10) NOT NULL,
    Email VARCHAR(30),

    PRIMARY KEY (ClientID)
);

CREATE TABLE Orders (
    OrderID CHAR(9) NOT NULL,
    EstimatedArrivalDate DATE,
    DateOrderReceived DATE NOT NULL,
    Quantity INTEGER NOT NULL,
    IsPremium BOOL NOT NULL,
    DeliveryAddress VARCHAR(80) NOT NULL,
    ShippingCost FLOAT NOT NULL,
    ClientID CHAR(9) NOT NULL,

    PRIMARY KEY (OrderID)
) ENGINE=InnoDB;

CREATE TABLE Courier (
    CourierID CHAR(9) NOT NULL,
    CourierName VARCHAR(50),
    CourierAddress VARCHAR(80) NOT NULL,
    Phone CHAR(10) NOT NULL,
    Email VARCHAR(30),
    TrackingLocationLat FLOAT,
    TrackingLocationLng FLOAT,

    PRIMARY KEY (CourierID)
);

CREATE TABLE Location (
    ProvinceCode CHAR(2) NOT NULL,
    WarehouseAddress VARCHAR(80) NOT NULL,
    Phone CHAR(10),
    Email VARCHAR(30),

    PRIMARY KEY (ProvinceCode)
);

CREATE TABLE Seller (
    SellerID CHAR(9) NOT NULL,

    PRIMARY KEY (SellerID)
);

CREATE TABLE ThirdPartySeller (
    SellerID CHAR(9) NOT NULL,
    SellerName VARCHAR(50) NOT NULL,
    SellerAddress VARCHAR(80) NOT NULL,
    Phone CHAR(10) NOT NULL,
    Email VARCHAR(30),

    PRIMARY KEY (SellerID)
);

CREATE TABLE Products (
    ProvinceCode CHAR(2) NOT NULL,
    ProductID CHAR(6) NOT NULL,
    DateReceived DATE,
    Cost FLOAT NOT NULL,
    Quantity INTEGER NOT NULL,
    SellingPrice FLOAT NOT NULL,
    DateShipping DATE,
    OrderID CHAR(9) NOT NULL,
    SellerID CHAR(9) NOT NULL,

    PRIMARY KEY (ProvinceCode, ProductID)
) ENGINE=InnoDB;

CREATE TABLE AssignOrder (
    OrderID CHAR(9) NOT NULL,
    CourierID CHAR(9) NOT NULL,

    PRIMARY KEY (OrderID, CourierID)
) ENGINE=InnoDB;

CREATE TABLE ThirdPartyItemsSold (
    SellerID CHAR(9) NOT NULL,
    ItemsSold VARCHAR(50) NOT NULL,

    PRIMARY KEY (SellerID, ItemsSold)
);

ALTER TABLE Orders
ADD FOREIGN KEY (ClientID) REFERENCES Client(ClientID) ON DELETE CASCADE;

ALTER TABLE ThirdPartySeller
ADD FOREIGN KEY (SellerID) REFERENCES Seller(SellerID);

ALTER TABLE Products
ADD FOREIGN KEY (ProvinceCode) REFERENCES Location(ProvinceCode),
ADD FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
ADD FOREIGN KEY (SellerID) REFERENCES Seller(SellerID);

ALTER TABLE AssignOrder
ADD FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
ADD FOREIGN KEY (CourierID) REFERENCES Courier(CourierID) ON DELETE CASCADE;

ALTER TABLE ThirdPartyItemsSold
ADD FOREIGN KEY (SellerID) REFERENCES ThirdPartySeller(SellerID);

INSERT INTO Client (ClientID, ClientName, ClientAddress, Phone, Email) VALUES
('BCIF00000', 'Imaginary Friend', '999 123rd Street', '1234567890', 'imaginary@email.com'),
('BCHL00001', 'Herbert Li', '8888 University Drive', '2789990897' , 'herbertli@email.com'),
('ONVV00002', 'Vishal Venkatakumar', '8888 University Drive', '253643789', 'vishal@email.com'),
('BCEH00003', 'Ekam Hothi', '666 420th Street', '9876543210', 'moreimaginary@email.com'),
('NSJS00003', 'Jack Sparrow', '145 Marine Drive', '1357832467', 'blackpearl@email.com');

INSERT INTO Orders (OrderID, EstimatedArrivalDate, DateOrderReceived, Quantity, IsPremium, DeliveryAddress, ShippingCost, ClientID ) VALUES
('BCGG00000', '2021-03-21', '2021-03-20', 3, TRUE, '999 123rd Street', 0, 'BCIF00000'),
('BCIF00001', '2021-08-09', '2021-07-01', 6, TRUE, '666 420th Street', 0, 'BCEH00003'),
('BCG00002', '2021-06-03', '2022-06-03', 5, TRUE,  '390 Avenue', 0, 'NSJS00003'),
('ONLL00003', '2021-05-21', '2021-02-15', 2, FALSE, '8777 University Drive', 24.5, 'ONVV00002'),
('ONXY00004', '2021-03-02', '2020-12-15', 10, FALSE, '1245 Main St.', 67.9, 'ONVV00002');

INSERT INTO Courier (CourierID, CourierName,  CourierAddress, Phone, Email, TrackingLocationLat, TrackingLocationLng) VALUES
('BCHP00000', 'Harry Potter', '8888 University Drive', 2934857291, 'potter@hogwarts.com', 57.797944, -124.541016),
('SKLF00001', 'Larry Fish', '7293 Example Rd.', 4637289485, 'fish@pacific.com', NULL, NULL),
('ONKE00001', 'Kanye East', '1111 My Way.', 2385920984, 'dabest@email.com', 50.026565, -85.253906),
('BCEA00001', 'Emily Anderson', '5555 Five Street.', 4203948593, 'emily@email.com', 50.866067, -123.574219),
('QCKK00001', 'Krusty Krab', '7777 Montreal St.', 2347893478, 'krab@email.com', NULL, NULL);


INSERT INTO AssignOrder (OrderID, CourierID ) VALUES
('BCGG00000', 'BCHP00000'),
('BCIF00001', 'BCHP00000'),
('BCG00002', 'BCHP00000'),
('ONLL00003', 'BCHP00000'),
('ONXY00004', 'BCHP00000'),
('BCIF00001', 'BCEA00001'),
('BCG00002', 'BCEA00001'),
('BCGG00000', 'ONKE00001'),
('BCIF00001', 'ONKE00001'),
('BCG00002', 'ONKE00001'),
('ONLL00003', 'ONKE00001'),
('ONXY00004', 'ONKE00001');

INSERT INTO Location (ProvinceCode, WarehouseAddress, Phone, Email) VALUES
('NT', '1124 Industrial Lane', 2738493748, NULL),
('BC', '2546 Hastings Rd.', 3829384958, 'bcwarehouse@email.com'),
('ON', '1111 Building Rd.', 2938492074, 'onwarehouse@email.com'),
('SK', '22435 Oakview Rd.', 3849504837, 'skwarehouse@email.com'),
('QC', '1342 Montreal Rd.',2839402839, 'qcwarehouse@email.com');

INSERT INTO Seller (SellerID) VALUES
('BC0000000'),
('BC0000001'),
('ON0000000'),
('ON0000001'),
('QC0000000'),
('SK0000000');

INSERT INTO ThirdPartySeller (SellerID, SellerName, SellerAddress, Phone, Email) VALUES
('BC0000000', 'Comfy Chair Inc.', '0001 Industrial Complex', '3829304829', 'headquarters@comfychair.com'),
('BC0000001', 'Extreme Sports', '2483 Adrenaline Lane', '2948394034', 'headquarters@extremesports.com'),
('ON0000000', 'GE Electronics', '2348 Road Rd.', '2839472930', 'headquarters@geelectronics.com'),
('QC0000000', 'Jake’s Jewelry', '0001 Industrial Complex', '3829304829', 'headquarters@comfychair.com'),
('SK0000000', 'Raj’s Yoga', '1234 Namastay Lane', '2839483942', 'headquarters@namastay.com');

INSERT INTO Products (ProvinceCode, ProductID, DateReceived, Cost, Quantity, SellingPrice, DateShipping, OrderID, SellerID) VALUES
('BC', '000001', '2021-01-22', 2.5, 20, 3, '2021-02-01', 'BCGG00000', 'BC0000000'),
('ON', '476125', '2021-01-23', 3, 27, 3, '2021-02-09', 'BCIF00001', 'BC0000001'),
('ON', '789125', '2021-01-20', 5.5, 30, 3, '2021-02-05', 'ONLL00003', 'ON0000000'),
('NT', '479135', '2021-01-21', 7.5, 15, 3, '2021-02-04', 'BCG00002', 'QC0000000'),
('BC', '524687', '2021-02-22', 4, 20, 3, '2021-03-01', 'ONXY00004', 'SK0000000');

INSERT INTO ThirdPartyItemsSold (SellerID, ItemsSold) VALUES
('BC0000000', 'Shoes'),
('BC0000001', 'Chocolates'),
('ON0000000','Mobile Phones'),
('QC0000000', 'Gaming Consoles'),
('SK0000000', 'Vacuum cleaners');

DELIMITER //

CREATE TRIGGER shipping_cost_check
BEFORE INSERT ON orders FOR EACH ROW
BEGIN
    IF NEW.SHIPPINGCOST > 100 THEN
        SET NEW.SHIPPINGCOST = 100;

END IF;

END//
