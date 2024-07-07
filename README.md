# Chaka (Car Selling Website)

I meticulously designed and implemented a suite of car buying functionalities, enabling users to effortlessly browse, select, and purchase vehicles with confidence. The database architecture I crafted is both scalable and efficient, underpinning the site's performance with a solid data management foundation.


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `https://chaka-back-end.onrender.com/car/list/` | `Json` | `Fetch All the Cars` |

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
