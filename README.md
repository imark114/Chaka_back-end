# Chaka (Car Selling Website)
 A robust and scalable backend system powering an innovative car selling platform. Developed using the powerful Django framework and Django REST Framework (DRF), this backend is designed to handle complex data interactions and provide seamless API endpoints for the frontend. With SQLite as the database engine, it ensures fast, reliable, and secure transactions. Whether it's managing car inventories, processing user queries, or handling sales transactions, CarHub's backend stands at the core of a smooth and efficient online car marketplace.


## API Reference

#### Get items

```http
  GET https://chaka-back-end.onrender.com/car/list/
```

| Id | Title | description | Drving mood | speed | Manufacture Date | Price | Brand |
| :-------- | :------- | :----| :-----| :-----| :-----| :-----| :-----|
| `1` | Corolla x | A masterful combination of style, power, sporty handling and comfort. | Auto | 250 | 2014-05-02 | 21000 |  Corolla |

#### Get Specific item

```http
  GET https://chaka-back-end.onrender.com/car/list/${id}
```
#### Registration

```http
  POST https://chaka-back-end.onrender.com/account/register/
```
#### Login

```http
  POST https://chaka-back-end.onrender.com/account/login/
```

#### Note:
    All other APIs are for authenticated users

## 🛠 Build With
Django, Django REST Framework
