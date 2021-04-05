# Art-ial - Testing Details #

Main [README.md](README.md) file.

View [website](https://art-ial-app.herokuapp.com/) deployed to Heroku.

---

## Contents ##

- [Art-ial - Testing Details](#art-ial---testing-details)
  - [Contents](#contents)
  - [Validation Services](#validation-services)
  - [Manual Testing](#manual-testing)
    - [User Stories Testing](#user-stories-testing)
    - [Compatibility and Responsiveness](#compatibility-and-responsiveness)
    - [Other Testing](#other-testing)
  - [Bugs](#bugs)
    - [Known Bugs](#known-bugs)
      - [1. Messages in all-auth templates are not showing](#1-messages-in-all-auth-templates-are-not-showing)
      - [2. Sold items in the bag](#2-sold-items-in-the-bag)
      - [3. Sold-out defence](#3-sold-out-defence)
    - [Solved Bugs](#solved-bugs)

## Validation Services ##

Additionally, all code was validated in the following ways:

HTML - All pages were successfully run through the [W3C HTML Validator](https://validator.w3.org/) to ensure compliance with the standards set by the W3C.

CSS - CSS validation with the [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/) returned some expected and necessary flags from vendor extensions. Other than that, the code complies to the W3C standards.

Python - All Python code was checked with the [PEP8 online validator](http://pep8online.com/) and is PEP8 compliant, aside from line length flags, which were left for code readability.

JavaScript - All files were tested with [JSHint](https://jshint.com/) validators.

## Manual Testing ##

### User Stories Testing ###

### Compatibility and Responsiveness ###

### Other Testing ###

## Bugs ##

### Known Bugs ###

#### 1. Messages in all-auth templates are not showing ####

- When a user takes actions, such as log in, logout, change password etc. The bug was discovered during the testing phase of the project. I have since identified that throughout the project I was using sweetify sweet-alerts and all-auth templates by default use messages as a form of notification. This is something I will be looking at a later stage of the development of this project and unable to fix due to time constrains as I would ideally like to use sweet-alerts and not have two forms of messaging in one application.

#### 2. Sold items in the bag ####

**Only happens if item sells elsewhere while a user has it sitting in the bag.*

- The intention of the app is to have one off pieces of artwork. Currently implemented code in checkout views is not completing the intended functionality which is meant to stop processing the checkout if one or more items in the bag are no longer available for sale. This can happen if two authentic users have the same item in the bag and user A checkouts successfully, leaving user B with the same item in the bag, which is now sold but yet user B bag is not updated.
  
    Current code does check these steps and does action redirect reverse with sweetify sweet-alerts notifications, and popping the sold items out of the bag however, the order still gets created, and the payment is taken, however user is not aware of that.

    You can find [buggy code here](https://github.com/neringabickmore/art-ial/pull/41/commits/efe613953a81b999ba1225a9c9b058934e9747af).

#### 3. Sold-out defence ####

- Shop template doesn't have a defence message if all items are sold out. I have attempted the following code to try and render the message, however what it did was show content even though there are items available for purchase.

**Closed Pull request #54*

```htmml

        {% for product in products %}
        <!-- if products are not sold show them -->
        {% if not product.is_sold %}
        {% include 'products/includes/products.html' %}
        <!-- if sold out -->
        {% elif product.is_sold %}
        <!-- only show once -->
        {% if forloop.first %}
        <div class="col-sm-12 px-4">
            <h4 class="my-4">Looks like we are out of stock.</h4>
            <p>Check again soon or contact us for enquiries.</p>
        </div>
        <div class="col-sm-12 px-4">
            <!-- enquire button -->
            <a class="btn my-3" href="/#contact-us-home" title="contact us" aria-label="enquire">enquire
                <span class="icon p-2">
                    <i class="fas fa-envelope" aria-hidden="true"></i>
                </span></a>
        </div>
        {% endif %}
        {% endif %}
        {% endfor %}
        
```

### Solved Bugs ###

- After W3S validation and error corrections in css files, available user emails in email management template were not showing. I have revered the CSS which fixed the error:

Before fix:

```CSS
.allauth-form-inner-content label:not([for='id_remember']),
.allauth-form-inner-content label:not([for^='email_radio_']) {
    display: none;
}
```

After fix:

```css
.allauth-form-inner-content label:not([for='id_remember'], [for^='email_radio_']) {

```

- **Templates path error in all-auth templates** During the testing of all-auth templates it became apparent that password-change, password-reset and password-reset-from-key templates were not re-directing the user to the shop as intended. This was due to the fact that during the development of the project I have changed the URL path in products app but my url path in all-auth templates was not dynamic to reflect the changes.

Before fix:

```HTML

<a class="btn my-2 col-sm-12" href="/shop/">
        <span class="icon p-2"><i class="fa fa-chevron-left"></i></span>go shopping
    </a>
```

After fix:

```HTML
<a class="btn my-2 col-sm-12" href="{% url 'shop' %}">
        <span class="icon p-2"><i class="fa fa-chevron-left"></i></span>go shopping
    </a>
```

**Applies to all site users:**

1. As a user, I am able to access the site on my mobile, tablet, and desktop which is adapted to provide the best experience.

2. As a user, I am able to easily navigate through the website without too much thought and find what I am looking for quickly.

3. As a user, I am able to identify instantly what the site is all about and what it has to offer.

4. As a user, I am able to contact the site owner using a simple form.

5. As a user, I am able to find key information about the artwork I am interested in (such as images, title, dimensions, etc)

6. As a user, I am able to add the artwork to my shopping bag, except if I am a superuser.

7. As a user, I am able to change the content of my shopping bag before continuing to completion (add more or remove the artwork), except if I am a superuser.

8. As a user, I am able to see a full breakdown of the total cost, including the shipping charge before proceeding to payment, except if I am a superuser.

9. As a user, I am able to purchase the artwork using my card in a secure environment, except if I am a superuser.

10. As a user, I am able to receive an email confirmation once I complete the payment, except if I am a superuser.

**Applies to new site users:**

1. As a user, I am able to  create an account.

**Applies to all returning users:**

1. As a user, I am able to login to my existing account and make a quicker purchase.

2. As a user, I am able to view, save and update my personal information.

3. As a user, I am able to view past orders, except if I am a superuser.

4. As a user, I am able to make purchases quicker by having stored information such as address, except if I am a superuser.

5. As a user, I am able to change or reset my password securely.

**Applies to a superuser (site owner):**

1. As a user, I am able to securely add, edit and delete the information for the specific artwork listed on the website.

2. As a user, I am able to change the tags on the products to specify new items to promote them.

3. As a user, I am able to receive inquiries from the site users after they fill in the contact form straight to my email inbox.

4. As a user, I am able to get an email with the customer orders when the purchases are made.

5. As a user, I am able to manipulate social media icons in the footer of the site (turn social media icons *on/off* and edit URLs).

6. As a user, I am able to edit content in the `About` section of the `Home` page.
