# ART.I.AL #

![ART.I.AL](/static/images/logo.jpg)

[ART.I.AL](https://art-ial-app.herokuapp.com/) - site description

Why I am doing this project

![Site display on different screens](/wireframes/testing-images/responsive-design.jpg)

---

## Contents ##

- [ART.I.AL](#artial)
  - [Contents](#contents)
  - [UX](#ux)
    - [Project Goals](#project-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [Site Visitor/User Goals](#site-visitoruser-goals)
    - [User Stories](#user-stories)
      - [**As a user (*applies to all site users*) I am able to:**](#as-a-user-applies-to-all-site-users-i-am-able-to)
      - [**As a new site user I am able to:**](#as-a-new-site-user-i-am-able-to)
      - [**As a returning user I am able to:**](#as-a-returning-user-i-am-able-to)
      - [**As a superuser (site owner) I am able to:**](#as-a-superuser-site-owner-i-am-able-to)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
      - [**Requirements**](#requirements)
      - [**Expectations**](#expectations)
    - [Design Choices](#design-choices)
      - [**Fonts**](#fonts)
      - [**Colours**](#colours)
  - [Wireframes](#wireframes)
    - [**Site Map**](#site-map)
    - [**Site Layout**](#site-layout)
  - [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Database Modelling](#database-modelling)
      - [**Profile App**](#profile-app)
        - [Profile](#profile)
      - [**Product App**](#product-app)
        - [Product](#product)
        - [Category](#category)
        - [Tag](#tag)
      - [Checkout App](#checkout-app)
        - [Order](#order)
        - [Order Line](#order-line)
  - [Technologies](#technologies)
    - [Languages](#languages)
    - [Libraries & Tools](#libraries--tools)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
    - [Future Features](#future-features)
  - [Changes applied since planning](#changes-applied-since-planning)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Deploying ART.I.AL to Heroku](#deploying-artial-to-heroku)
  - [Credits](#credits)
    - [Images](#images)
    - [Image editing](#image-editing)
    - [Code ideas](#code-ideas)
  - [Acknowledgements](#acknowledgements)

---

## UX ##

### Project Goals ###

This project is my final project for the Code Institute's Full stack development programme. The main goal of this project is to create an e-commerce site using Django framework, which is hosted with AWS as well as implementing a fully functional payment system with Stripe.

At the beginning of 2020, my sister started experimenting with paint on canvases that has now gained popularity amongst family, friends, colleagues as well as enquiries from her followers on Instagram. I have therefore decided to commit in creating a website for my sister as a professional platform to sell her artwork. After my graduation, this site will be used as fully functional e-commerce platform.

### Site Owner Goals ###

- Provide the users with a professional e-commerce online shop to allow secure purchases
- Make profit selling artwork
- Promote the artwork and the brand of the artist

### Site Visitor/User Goals ###

- View new artwork produced by the artist
- Ability to buy artwork online

### User Stories ###

#### **As a user (*applies to all site users*) I am able to:** ####

1. Access the site on my mobile, tablet and desktop which is adapted to provide the best experience.

2. Easily navigate through the website without too much thought and find what I am looking for quickly.

3. Identify instantly what the site is all about and what it has to offer.

4. Contact the site owner using a simple form.

5. Find key information about the artwork I am interested in (such as images, title, dimensions, etc)

6. Filter the artwork in the gallery page to identify new, available, and sold artwork.

7. Add the artwork in my shopping bag.

8. Change the content of my shopping bag before continuing to completion (add more or remove the artwork).

9. See full breakdown of the total cost, including the shipping charge before proceeding to payment.

10. Purchase the artwork using my card in a secure environment.

11. Receive an email confirmation once I complete the payment.

#### **As a new site user I am able to:** ####

1. Create an account.

#### **As a returning user I am able to:** ####

1. Login to my existing account and make a quicker purchase.

2. View, save, and update my personal information.

3. View past orders.

4. Make purchases quicker by having stored information such as address.

5. Change or reset my password securely.

#### **As a superuser (site owner) I am able to:** ####

1. Securely add, edit and delete the information for the specific artwork listed on the website.

2. Change the tags on the products to specify new, available, an sold artwork.

3. Receive enquiries from the site users after they fill in the contact form straight to my email inbox.

4. Get an email with the customer orders when the purchases are made.

[Back to content](#contents)

### User Requirements and Expectations ###

#### **Requirements** ####

- Visually pleasant app design
- Easy site navigation
- Information of the content layed out in a simple and clear way on both mobile and larger screens
- Self-explanatory icons where text is absent

#### **Expectations** ####

- User information is protected by the site
- User is able to manipulate elements of the particular page
- Quick app load time

[Back to content](#contents)

### Design Choices ###

#### **Fonts** ####

- *Headers, titles*

  ```font-family: 'Krona One', sans-serif;```

- *Paragraphs, descriptions*

  ```font-family: 'Exo', sans-serif;```

#### **Colours** ####

![Colour palette](/wireframes/colour-palette/colour-palette.jpg)

[Back to content](#contents)

## Wireframes ##

### **Site Map** ###

Firstly, I have created a site [map](/wireframes/site-map/sitemap.png) to identify clear features the site will have when viewed by the visitor, registered user, and admin.

### **Site Layout** ###

I designed my site moc-ups using [balsamiq wireframes](https://balsamiq.com/). I was focusing on defining the basic layout structure of the app and identifying how displays would change on different screen sizes such as [mobile](/wireframes/site-wireframes/gallery-buy.mobile.png), [tablet](/wireframes/site-wireframes/gallery-buy.tablet.png), and [desktop](/wireframes/site-wireframes/gallery-buy.desktop.png)

You can view all wireframes created for this project in [site wireframes](/wireframes/site-wireframes) folder.

[Back to content](#contents)

---

## Information Architecture ##

### Database Choice ###

### Database Modelling ###

#### **Profile App** ####

##### Profile #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
 Username | username | OneToOneField 'User' |  on_delete=models.CASCADE
 Full Name | profile_full_name | CharField | max_length=70, null=True, blank=True
 Phone number | profile_phone_number | CharField | max_length=20, null=True, blank=True
 Address Line1 | profile_address_line1 | CharField | max_length=60, null=True, blank=True
 Address Line2 | profile_address_line2 | CharField | max_length=60, null=True, blank=True
 Town/City | profile_town_or_city | CharField | max_length=50, null=True, blank=True
 County | profile_county | CharField | max_length=50, null=True, blank=True
 Postcode | profile_postcode | CharField | max_length=20, null=True, blank=True
 Country | profile_country | CountryField | blank_label='Country', null=True, blank=True

#### **Product App** ####

##### Product #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
 Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL
 Title | title | CharField | max_length=254
 Description | description | TextField | max_length=800
 Dimensions | dimensions | CharField | max_length=70, null=True, blank=True
 Price | price | DecimalField |max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)]
 Image | image| ImageField | null=True, blank=True
 Image Url | image_url | URLField | max_length=1024, null=True, blank=True
 Sku | sku | CharField | max_length=254, null=True, blank=True
 Tag| tag | CharField | max_length=50, null=True, blank=True

##### Category #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Programmatic Name | name | CharField | max_length=50
Friendly Name | friendly_name | CharField | max_length=50, null=True, blank=True

##### Tag #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Programmatic Name | name | CharField | max_length=50
Friendly Name | friendly_name | CharField | max_length=50, null=True, blank=True

#### Checkout App ####

##### Order #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Order Number | order_number | CharField | max_length=32, null=False, editable=False
Profile | profile | ForeignKey 'Profile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
Full Name | full_name | CharField | max_length=70, null=False, blank=False
Email | email | EmailField | max_length=254, null=False, blank=False
Phone number | phone_number | CharField | max_length=20, null=False, blank=False
Address Line1 | address_line1 | CharField | max_length=60, null=False, blank=False
Address Line2 | address_line2 | CharField | max_length=60, null=False, blank=False
Town/City | town_or_city | CharField | max_length=50, null=False, blank=False
County | county | CharField | max_length=50, null=True, blank=True
Postcode | postcode | CharField | max_length=20, null=True, blank=True
Country | country | CountryField | blank_label='Country*', null=False, blank=False
Purchase Date | purchase_date | DateTimeField | auto_now_add=True
Delivery Cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
Order Total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Grand Total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Original Cart | original_cart | TextField | null=False, blank=False, default=''
Stripe Pid | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''
Comment | comment | TextField | max_length=254, null=True, blank=True

##### Order Line #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Order | order | ForeignKey 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product | product | ForeignKey 'Product' | null=False, blank=False, on_delete=models.PROTECT
Item Total | item_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False
Datetime | datetime | CharField | null=True, blank=True, max_length=20

[Back to content](#contents)

---  

## Technologies ##

### Languages ###

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

### Libraries & Tools ###

- [jQuery](https://jquery.com/)
- [Popper](https://popper.js.org/)
- [Popper JS](https://popper.js.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Flask](https://www.fullstackpython.com/flask.html)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [Font-Awesome](https://fontawesome.com/icons?d=gallery)
- [Google fonts](https://fonts.google.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Heroku](https://www.heroku.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Color editor](https://coolors.co/)
- [Image editor](https://www.birme.net/)

[Back to content](#contents)

---

## Features ##

Art-ial website is designed using five applications: `home`, `products`, `profiles`, `bag`, `checkout`.

### Implemented Features ###

- **Responsive design**

The app has a different layout options, focused on *mobile-first* design in mind as more users are expected to use mobile rather than larger devices, such as a tablet or a laptop/desktop.

- **Register** account form

- **Sign in/out** functionality

- **Easy navigation** to external sites

The user is redirected to a website when clicks on *purchase* a book button.

- **Defence mechanism**

- **Site admin** edit

Site admin feature allows deletion of inappropriate reviews, change of book review form items, as well as deletion of the registered user accounts.

### Future Features ###

- **Language Selector**
  
The user is able to choose English or Lithuanian language to view the site.

- **Password re-set**

- **Search function**

The user is able to search books by entering any text that may appear on the book review (i.e. author, title, length, genre etc).

[Back to content](#contents)

---

## Changes applied since planning ##

---

## Testing ##

Testing information can be found in a separate [Testing.md](Testing.md) file.

[Back to content](#contents)

---

## Deployment ##



### Deploying ART.I.AL to Heroku ###

1: **Login** to Heroku and create a new app.

2: **Create** a requirements.txt file using the following command:

```
pip3 freeze --local > requirements.txt
```

3: **Create** a Procfile with the following command:

```
echo web: python run.py > Procfile
```

4: **Push** these newly created files to your repository master.

5: **Add heroku remote** to your git repository by getting the heroku git URL from the heroku account settings. Then type the following: 

```
git remote add heroku https://git.heroku.com/your-heroku-repo
```

6: Push *ART.I.AL* to your heroku:

```
git push heroku master
```

7: In your heroku app, **set** the following variables:

**Key**|**Value**
:-----:|:-----:
HOSTNAME|0.0.0.0
PORT|5000
SECRET_KEY|YOUR_SECRET_KEY

  ** Please make sure you enter your own *SECRET_KEY*, and **.

8: Click the deploy button on the Heroku dashboard.
9: The site has been deployed the Heroku.

[Back to content](#contents)

---

## Credits ##

### Images ###

### Image editing ###

- I have used the snippet tool for capturing screengrabs which I saved as images.
- MS Paint 3D to edit images as required.
- A handy [Birme](https://www.birme.net/?target_width=300&target_height=300&quality=100&border_width=1&border_color=%23bd3d3a) site allowed me to resize the images all at once.
- I have also used [giphy.com](https://giphy.com/) to convert MP4 video files to gif files used in Testing.md.

### Code ideas ###


[Back to content](#contents)

---

## Acknowledgements ##


[Back to content](#contents)
