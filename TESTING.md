# Art-ial - Testing Details #

Main [README.md](README.md) file.

View [website](https://art-ial-app.herokuapp.com/) deployed to Heroku.

---

## Contents ##

- [Art-ial - Testing Details](#art-ial---testing-details)
  - [Contents](#contents)
  - [Manual Testing](#manual-testing)
    - [Responsiveness](#responsiveness)
    - [Navbar](#navbar)
    - [Footer](#footer)
    - [Home Page](#home-page)
    - [Shop Page](#shop-page)
    - [Gallery Page](#gallery-page)
    - [Product Details Page](#product-details-page)
    - [Bag Page](#bag-page)
    - [Checkout & Checkout Success](#checkout--checkout-success)
    - [User Authentication Pages](#user-authentication-pages)
    - [Profiles Pages](#profiles-pages)
    - [Superuser Site Management Functionality (CRUD)](#superuser-site-management-functionality-crud)
  - [Validation Services](#validation-services)
  - [Compatibility and Responsiveness](#compatibility-and-responsiveness)
    - [Other Testing](#other-testing)
  - [Bugs](#bugs)
    - [Known Bugs](#known-bugs)
    - [Solved Bugs](#solved-bugs)

## Manual Testing ##

### Responsiveness ###

- **📖 User story:**
  
    *As a user, I am able to access the site on my mobile, tablet, and desktop which is adapted to provide the best experience.*

- **🧪 Test:**
  
  - Chrome Dev tools used to view the layout of the site on all resolutions available.
  - Please see [Compatibility and Responsiveness](#compatibility-and-responsiveness) for more detailed information.

- **📌 Result:**
  
    This test was performed continuously throughout the development of the application. Wherever required, I made styling adjustments to ensure the user story is complete.

- **✅ Verdict:**

    The issues were successfully fixed and all tests passed.

### Navbar ###

- **📖 User story:**

    *As a user, I am able to easily navigate through the website without too much thought and find what I am looking for quickly.*

- **🧪 Test:**
  - Click on all of the available links in the navbar. Assess if they are directing you to the page/section of the page you expect it.
  - Try clicking on the navbar both on mobile and larger devices.
  - Larger than medium screen size devices should have all navbar item displayed at all times.
  - Small and medium screen size should have a collapsible navbar.
  - All navbar items should change colour from white to light pink (tuscany) on hover on all screen sizes.
  - If you haven't logged in, you should see `Login` on a navbar.
  - If you have logged in, you should see `Profile` on a navbar instead of login, which expands to `Account` and `Logout`.
  - If you are not a superuser, you should see `Home`, `Gallery`, `Shop`, `About`, `Contact` and `Login` or `Profile` on a navbar.
  - If you are a superuser, you should see `Home`, `Gallery`, `Management` which expands to `Products`, `Social Media` and `Order history`, and `Profile`, which expands to `Account` and `Logout`.
  - If you have items added to the bag, you should see a bag icon and a total amount.

- **📌 Result and ✅Verdict**

    All tests passed, no bugs were found at the final round of testing.

### Footer ###

- **📖 User story:**
   As a user, I am able to easily navigate through the website without too much thought and find what I am looking for quickly.

- **🧪 Test:**

  - Click on `Quicklinks`. They should direct you to relevant parts of the site.
  - Click on the `Instagram` icon, currently the only active social media account Art-ial has. It should direct you to the account.
  - when you hover on `Quicklinks` and `Instagram` it should change colour to green (hunter-green)

- **📌 Result and ✅Verdict**

    All tests passed, no bugs were found at the final round of testing.

### Home Page ###

- **📖 User story:**

    *As a user, I am able to contact the site owner using a simple form.*

    *As a user, I am able to identify instantly what the site is all about and what it has to offer.*

    *As a user (super-user), I am able to edit content in the `About` section of the `Home` page.*

    *As a user, I am able to receive inquiries from the site users after they fill in the contact form straight to my email inbox.*

- **🧪 Test:**

  - when you navigate on `Home` page or click on the `logo`, you should be directed to the home page.
  - Navbar items on the navbar should also give a good idea to the user what the site is all about (`Gallery`, `Shop`).
  - You should be able to see a video of nature at the top of the page followed by the `About` section. When hovered on the `Video`, the user should notice a small tooltip on the right side bottom of the image saying `go shopping` and if clicked is taken to the `Shopping` page.
  - The `About` section should have a summary of the author.
  - If you are a superuser, you should see a button `Edit` which takes you to another page where you can edit the content (title and description) of what is displayed in this section of the page. If you delete the content, the section would remain empty, I, therefore, advise you to always have some content about the offer in this section.
  - You should see the `Contact` form right before the footer. If you are not logged in, all fields of the form should be empty. If you are a registered user and have logged in, you should have **full name** (if entered) and **email** sections pre-filled.
  - The form should give errors if you click `Send` and any parts of the form are missing, not correct information provided or the consent form is un-ticked.
  - If the form is correct and is submitted, the site owner (superuser) receives an email with the message, with customers details in the header.
  - The user receives **Success** on the screen after the message is sent.

- **📌 Result:**

  - All buttons worked as intended and redirected the user to correct parts of the site as intended.
  - If logged in as a superuser, you can see `edit` button and change content in the redirected page. If you delete the content, the section would remain empty, I, therefore, advise you to always have some content about the offer in this section.
  - Contact form shows elements as described above and as intended.
  - The user receives error messages if the form is not correct.
  - If the form is correct and the message is sent successfully, the user sees **Success** message and the site owner (superuser) receives an email.

- **✅ Verdict:**
  
  All tests passed and functionality worked as intended.

### Shop Page ###

- **📖 User story:**

    *As a user, I am able to find key information about the artwork I am interested in (such as images, title, dimensions, etc)*

    *As a user, I am able to add the artwork to my shopping bag, except if I am a superuser.*

- **🧪 Test:**

  - This page should not be visible to a superuser by default and removed on purpose as there isn't any specific functionality that would require them to have it as required by default. However, the superuser can access this page if they know a url path.
  - You should only see items that are available for sale on this page and not see any items that have been sold.
  - You should be able to see basic information about the painting (Collection: Title) and the `View details` button.
  - If you hover over the painting, the image should fade and you should see *hand* pointer with title *view details* and able to click on the image.
  - If you click on the image or `view details` you should get redirected to the product details page. This is the only way you should be able to access a product details page.

- **📌 Result and ✅Verdict**

    All tests passed, no bugs were found at the final round of testing.

### Gallery Page ###

- **📖 User story:**

    *As a user, I am able to find key information about the artwork I am interested in (such as images, title, dimensions, etc)*

    *As a user, I am able to securely add, edit and delete the information for the specific artwork listed on the website.*

    *As a user, I am able to change the tags on the products to specify new items to promote them.*

- **🧪 Test:**

  - If you are logged in as a superuser:
    - You should be able to see all of the artwork that is available on the site with buttons `Edit` and `Delete` product underneath every product image (on small and large devices, but the right side of the screen on medium-sized)
    - If you click on `Edit`, it should redirect you to `Product Management` -> `Edit Product`. The form you see should already be pre-filled. At the bottom of the page you should see `Go back` and `Update` buttons, which should take you back to the `Gallery` page.
    - If you chose to update the info, the information you see on a re-direction should have new content and a notification that your product was updated.
    - When editing the content of the product, you should try entering an existing name of another painting and if you do so, you should get a notification that the product name already exists and the form would not submit.
    - If you leave any mandatory fields empty and try to submit the form, you should also get a notification to check the fields and the form would not submit.
    - If the form was entered correctly, you should receive a success message and get redirected to `Gallery`.
    - If you clicked on `Go back`, the content shouldn't have changed or you should see any messages.
    - If you click on `delete product` you should get a pop-up message asking to reconfirm your intentions to delete a product and should require you to click on the `yes, delete` button if this was your intention or the `no, go back` if you made a mistake.
  - If you are not logged in at all or logged as authenticated user or superuser:
    - You should be able to see basic information about the painting (Collection: Title) and the `View details` button.
    - You should be able to see all of the items (including sold) in this part of the site.
    - If you hover over the painting, the image should fade and you should see *hand* pointer with title *view details* and able to click on the image.
    - If you click on the image or `view details` you should get redirected to the product details page. This is the only way you should be able to access a product details page.
  
- **📌 Result:**

    Functionalities intended for the superuser were only accessible by the user with superuser status. All other users had limited functionalities at this stage as intended.

    All superuser functionalities worked as intended, including the `delete` button. This was built to prevent mishaps.

    If the non-superuser tried to access edit/delete functionalities, they should not be able to do this and get a notification that this functionality is only accessible by the superusers.

- **✅ Verdict:**

  All tests passed and functionality worked as intended.

### Product Details Page ###

- **📖 User story:**

    *As a user, I am able to find key information about the artwork I am interested in (such as images, title, dimensions, etc)*

    *As a user, I am able to securely add, edit and delete the information for the specific artwork listed on the website.*

    *As a user, I am able to change the tags on the products to specify new items to promote them.*

- **🧪 Test:**

- **📌 Result:**

- **✅ Verdict:**

### Bag Page ###

- **📖 User story:**
  
  *As a user, I am able to change the content of my shopping bag before continuing to completion (add more or remove the artwork), except if I am a superuser.*

  *As a user, I am able to see a full breakdown of the total cost, including the shipping charge before proceeding to payment, except if I am a superuser.*

- **🧪 Test:**

- **📌 Result:**

- **✅ Verdict:**

### Checkout & Checkout Success ###

- **📖 User story:**

    *As a user, I am able to see a full breakdown of the total cost, including the shipping charge before proceeding to payment, except if I am a superuser.*

    *As a user, I am able to purchase the artwork using my card in a secure environment, except if I am a superuser.*

    *As a user, I am able to receive an email confirmation once I complete the payment, except if I am a superuser.*

- **🧪 Test:**

- **📌 Result:**

- **✅ Verdict:**

### User Authentication Pages ###

- **📖 User story:**

   *As a user, I am able to  create an account.*

   *As a user, I am able to change or reset my password securely.*

   *As a user, I am able to view, save and update my personal information.*

- **🧪 Test:**

- **📌 Result:**

- **✅ Verdict:**

### Profiles Pages ###

- **📖 User story:**

    *As a user, I am able to  create an account.*

    *As a user, I am able to change or reset my password securely.*

    *As a user, I am able to login to my existing account and make a quicker purchase.*

    *As a user, I am able to view, save and update my personal information.*

    *As a user, I am able to view past orders, except if I am a superuser.*

    *As a user, I am able to make purchases quicker by having stored information such as address, except if I am a superuser.*

    *As a user, I am able to change or reset my password securely.*

- **🧪 Test:**

- **📌 Result:**

- **✅ Verdict:**

### Superuser Site Management Functionality (CRUD) ###

- **📖 User story:**

*As a user, I am able to securely add, edit and delete the information for the specific artwork listed on the website.*

*As a user, I am able to change the tags on the products to specify new items to promote them.*

*As a user, I am able to get an email with the customer orders when the purchases are made.*

*As a user, I am able to manipulate social media icons in the footer of the site (turn social media icons **on/off** and edit URLs).*

- **🧪 Test:**

- **📌 Result:**

- **✅ Verdict:**

## Validation Services ##

Additionally, all code was validated in the following ways:

HTML - All pages were successfully run through the [W3C HTML Validator](https://validator.w3.org/) to ensure compliance with the standards set by the W3C.

CSS - CSS validation with the [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/) returned some expected and necessary flags from vendor extensions. Other than that, the code complies to the W3C standards.

Python - All Python code was checked with the [PEP8 online validator](http://pep8online.com/) and is PEP8 compliant, aside from line length flags, which were left for code readability.

JavaScript - All files were tested with [JSHint](https://jshint.com/) validators.

## Compatibility and Responsiveness ##

The following tools were used to continuously test the compatibility and responsiveness of the site:

1. Google Chrome developer tools on HP Envy
2. Mobile phone (Huawei P30 Pro, Iphone X)
3. tablet (iPad)
4. Multiple browsers (Chrome, Safari, FireFox, Chromium and Vivaldi )
5. Am I Responsive (Had to use ngrok to test the feature as Heroku has restrictions)

***Note***:

- *Apple devices were overriding CSS on `trash` button in a shopping bag.*

- *Video banner on `home` page originally had sound on, however as auto-play wasn't compatible across all browsers without default mute, I have decided to mute it by default.*

### Other Testing ###

- **DEBUG**

    Throughout the development process, `DEBUG` was continuously on. This has allowed continuously allowed me to notice site crashes, identify where the error was and enable me to fix it wherever possible.

- **Unique users**

    I have also had fellow students, family and friends thoroughly test my site. They have noticed some incredible errors I have naturally missed which allowed me to improve the code. All the errors and bugs discovered are written up in **Bugs** section. Also, I was given some advice on features of my site that has convinced me to reconsider elements of the layout of the site, colours, fonts and content (i.e. `Home` app.). All feedback considered, I was able to improve functionalities and UX.

## Bugs ##

### Known Bugs ###

Bugs below I have discovered throughout the development of the site and I was unable to fix yet. I have spend many of hours, slack community support and tutors to be able to fix it, however, I was not able to invest more time into this at the precise moment.

- **🐞 500.html**
  
  Template 500.html doesn't work. It is placed in root template just as is 404.html, however, it's not working.

- **🐞 Messages in all-auth templates are not showing**

    When a user takes actions, such as login, logout, change password etc. The bug was discovered during the testing phase of the project. I have since identified that throughout the project I was using sweetify sweet-alerts and all-auth templates by default use messages as a form of notification. This is something I will be looking at a later stage of the development of this project and unable to fix due to time constraints as I would ideally like to use sweet-alerts and not have two forms of messaging in one application.

- **🐞 Sold items in the bag**

    **Only happens if an item sells elsewhere while a user has it sitting in the bag.*

    The intention of the app is to have one off pieces of artwork. Currently implemented code in checkout views is not completing the intended functionality which is meant to stop processing the checkout if one or more items in the bag are no longer available for sale. This can happen if two authentic users have the same item in the bag and user A checkouts successfully, leaving user B with the same item in the bag, which is now sold but yet user B bag is not updated.
  
    Current code does check these steps and does action redirect reverse with sweetify sweet-alerts notifications, and popping the sold items out of the bag however, the order still gets created, and the payment is taken, however the user is not aware of that.

    You can find [buggy code here](https://github.com/neringabickmore/art-ial/pull/41/commits/efe613953a81b999ba1225a9c9b058934e9747af).

- **🐞 Sold-out defence**

  Shop template doesn't have a defence message if all items are sold out. I have attempted the following code to try and render the message, however, what it did was show content even though there are items available for purchase.

    **Closed Pull request #54*

    ```HTML

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

- **Product image url paths**

    **🐞 Bug:**

    Images Model has boolean fields that state if an image is `main` or if it is `room-view`. the original code for `product-image` if it has URL was rendering both the image which is set to be main as well as if the image isn't set to be main as it was not an intention for it to render in such way.

    ```HTML
        {% for img in item.product.images_folder.imgs.all %}
        {% if img.main_img %}
        <img class="img-fluid bag-image" src="{{ img.url }}" alt="{{ item.product.name }}">
        {% else %}
        <img class="img-fluid" src="{{ MEDIA_URL }}noimage.png" alt="{{ item.product.name }}">
        {% endif %}
        {% endfor %}
    ```

    **🔨 Fix:**

    ```HTML
        {% for img in item.product.images_folder.imgs.all %}
        {% if img.main_img %}
        <img class="img-fluid bag-image" src="{% if img.url %}{{ img.url }}{% else %}{{ MEDIA_URL }}noimage.png{% endif %}"
            alt="{{ item.product.name }}">
        {% endif %}
        {% endfor %}
    ```

    **✅ Verdict:**

    The bug was successfully fixed and all test passed.

- **Checkout form buttons**
  
  **🐞 Bug:**
  
  While I was working on minimising the code I have decided to create submit button include for the checkout form without taking much notice that buttons cannot be reused in a way as I intended as they had specific different IDs.

  **🔨 Fix:**

  Reversed the code to one button per required field instead of creating an include:

  ```HTML
    <!--Button Next-->
    <button type="submit" id="personal-details-btn" class="btn checkout-btn">
        <span class="text-uppercase">next</span>
        <span class="icon p-2">
            <i class="fas fa-chevron-right" aria-hidden="true"></i>
        <span class="text-uppercase">back</span>
    </a>
    <!-- Next button -->
    <button type="submit" id="delivery-info-btn" class="btn checkout-btn">
        <span class="text-uppercase">next</span>
        <span class="icon p-2">
            <i class="fas fa-chevron-right" aria-hidden="true"></i>
    </button>
  ```

    **✅ Verdict:**

    The bug was successfully fixed and all test passed.

- **Add product - unique name**

    **🐞 Bug:**
    In my `add-poduct` view I wanted the system to double-check the database if the product doesn't already exist in the system before adding it to the DB. I ran into a few problems when working through this solution:
    1. Product models were not explicit to allow unique names only in the names entered in the particular model. I have identified this as a particularly important feature that I need to fix to prevent the repeat of the names.
    2. Edit product was not handling `product.name` as it was supposed to on `form-post`.

    **🔨 Fix:**

    1. Here is an example of the code used to fix the issue, where I have included `unique=True` when defining the elements of the model. This prevents names to be repeated in the particular model by default.

    ```python

    class Category(models.Model):

    class Meta:
        verbose_name_plural = "Product Categories"

    name = models.CharField(max_length=50, unique=True)
    friendly_name = models.CharField(
        max_length=50, null=True, blank=True)
    ```

    1. View `edit_product` was changed to call for `product_id` rather than name and therefore the views and Html was changed as follows in python files (snippet that's important. you can find full view [here](https://github.com/neringabickmore/art-ial/blob/master/products/views.py#L124)):

    ```python
    view.py:

    @login_required
    def edit_product(request, product_id):
        """ Edit product details """

        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            prod_form = ProductForm(request.POST, instance=product)
            if prod_form.is_valid():
                prod_form.save()
                sweetify.sweetalert(
                    request, icon='success',
                    title="Successfully updated product details!")
                return redirect(reverse('product_detail', args=[product.name]))

        template = 'products/prod-mngmnt/edit-product.html'
        context = {
            'prod_form': prod_form,
            'product': product,
            'all_social_media': social_media,
        }

    return render(request, template, context)
    
    url.py:
    path(
        'edit/product/<int:product_id>/', views.edit_product,
        name='edit_product'),

    ```

    and the template:

    ```HTML
    <form method="POST" action="{% url 'edit_product' product.id %}" class="form mb-2 prod-mngmnt-form">   
    ```

    **✅ Verdict:**

    The bug was successfully fixed and all test passed.

- **Product add/view button**

    **🐞 Bug:**

    During the development stage of the product, I have come up with a better UX idea for the user and swap button from `add to bag` to `view bag` if the user has added the item to their shopping bag, although I do have a defence built in my views to prevent the user adding the same item twice.

    **🔨 Fix:**

    Added additional code in product views to allow to check which button to show in Html:

    ```python

    show_add_btn = True

        if str(product.id) in bag:
            show_add_btn = False

    ```

    ```HTML

        {% if show_add_btn %}
            <!-- If product is not in the bag, show add btn -->
            <button class="btn col-12 my-3" type="submit">Add to bag<span
                    class="icon p-2">
                    <i class="fas fa-plus" aria-hidden="true"></i>
                </span></button>
            {% else %}
            <!-- If product is in the bag show view bag -->
            <a class="btn col-12 col-sm-4 my-3" href="{% url 'view_bag' %}">view bag<span
                    class="icon p-2">
                    <i class="fas fa-chevron-right" aria-hidden="true"></i>
                </span></a>
            {% endif %}

    ```

    **✅ Verdict:**

    The bug was successfully fixed and all test passed.

- **All-auth template - email**

    **🐞 Bug:**

     After W3S validation and error corrections in css files, available user emails in email management template were not showing. I have revered the CSS which fixed the error:

    ```CSS
    .allauth-form-inner-content label:not([for='id_remember']),
    .allauth-form-inner-content label:not([for^='email_radio_']) {
    display: none;
    }
    ```

    **🔨 Fix:**

    ```css
    .allauth-form-inner-content label:not([for='id_remember'], [for^='email_radio_']) {

    ```

    **✅ Verdict:**

    The bug was successfully fixed and all test passed.

- **Templates path error in all-auth templates**

    **🐞 Bug:**

  During the testing of all-auth templates it became apparent that password-change, password-reset and password-reset-from-key templates were not re-directing the user to the shop as intended. This was due to the fact that during the development of the project I have changed the URL path in products app but my url path in all-auth templates was not dynamic to reflect the changes.

    ```HTML

    <a class="btn my-2 col-sm-12" href="/shop/">
            <span class="icon p-2"><i class="fa fa-chevron-left"></i></span>go shopping
        </a>
    ```

    **🔨 Fix:**

    ```HTML
    <a class="btn my-2 col-sm-12" href="{% url 'shop' %}">
            <span class="icon p-2"><i class="fa fa-chevron-left"></i></span>go shopping
        </a>
    ```

    **✅ Verdict:**

    The bug was successfully fixed and all test passed.
