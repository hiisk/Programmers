SELECT cart_id from CART_PRODUCTS
where cart_id in (select cart_id from CART_PRODUCTS where name = 'Yogurt') and name = "Milk"
order by 1