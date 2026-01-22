# TODO

[ ] Introduction page/home page
[ ] Register page
[ ] Login page
[ ] Store + Search + Reviews + Movie info
[ ] Shopping cart
[ ] Tracker
[ ] Review section + edit + delete + report
[ ] Admin (given)

## Endpoints

Note: `id` is for movies, `rid` is for reviews.

[ ] admin/
[ ] auth/
    - register
    - login
    - logout
[ ] /
[ ] cart/
    - add (?id)
    - remove (?id, ?all)
    - order
[ ] tracking/
[ ] store/
    - movie (?id)
[ ] reviews/
    - add (?id)
    - remove (?rid)
    - update (?rid)
    - fetch (?id)
[ ] admin/

## Views

[ ] home
[ ] cart
[ ] tracking
[ ] admin
[ ] reviews (?)
[ ] register
[ ] login

layout.html -> store, cart (logged in), tracking (logged in), logout (logged in), home, admin, register
style.css (split device size)

## Models

[ ] Movie (title, date, id, image, avg. rating, price)
[ ] User
[ ] CartItem (?)
[ ] Cart (list Movie-s/CartItem-s) (?)
[ ] Review (rid, id, review_value (float >=5.0/10.0))
[ ] Order (list Movie-s, price, date)

