<!-- TODO: Applies to all site users:
1. As a user, I am able to access the site on my mobile, tablet, and desktop which is adapted to provide the best experience.
2. As a user, I am able to easily navigate through the website without too much thought and find what I am looking for quickly.
1. As a user, I am able to identify instantly what the site is all about and what it has to offer.
2. As a user, I am able to contact the site owner using a simple form.
3. As a user, I am able to find key information about the artwork I am interested in (such as images, title, dimensions, etc)
4. As a user, I am able to add the artwork to my shopping bag, except if I am a superuser.
5. As a user, I am able to change the content of my shopping bag before continuing to completion (add more or remove the artwork), except if I am a superuser.
6. As a user, I am able to see a full breakdown of the total cost, including the shipping charge before proceeding to payment, except if I am a superuser.
7. As a user, I am able to purchase the artwork using my card in a secure environment, except if I am a superuser.
8.  As a user, I am able to receive an email confirmation once I complete the payment, except if I am a superuser.
TODO: Applies to new site users:
1. As a user, I am able to  create an account.
**Applies to all returning users:**
1. As a user, I am able to login to my existing account and make a quicker purchase.
2. As a user, I am able to view, save and update my personal information.
3. As a user, I am able to view past orders, except if I am a superuser.
4. As a user, I am able to make purchases quicker by having stored information such as address, except if I am a superuser.
5. As a user, I am able to change or reset my password securely.
TODO: Applies to a superuser (site owner):
1. As a user, I am able to securely add, edit and delete the information for the specific artwork listed on the website.
2. As a user, I am able to change the tags on the products to specify new items to promote them.
3. As a user, I am able to receive inquiries from the site users after they fill in the contact form straight to my email inbox.
4. As a user, I am able to get an email with the customer orders when the purchases are made.
5. As a user, I am able to manipulate social media icons in the footer of the site (turn social media icons *on/off* and edit URLs).
6. As a user, I am able to edit content in the `About` section of the `Home` page.
-->

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
    - [Solved Bugs](#solved-bugs)

## Validation Services ##

Additionally, all code was validated in the following ways:

HTML - All pages were successfully run through the [W3C HTML Validator](https://validator.w3.org/) to ensure compliance with the standards set by the W3C.

CSS - CSS validation with the [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/) returned some expected and necessary flags from vendor extensions. Other than that, the code complies to the W3C standards.

Python - All Python code was checked with the [PEP8 online validator](http://pep8online.com/) and is PEP8 compliant, aside from line length flags, which were left for code readability.

JavaScript - All files were tested with [JSHint](https://jshint.com/) validators.

## Manual Testing ##

### User Stories Testing ###

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

    **✅  Verdict:**

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

    **✅  Verdict:**

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

    **✅  Verdict:**

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

    **✅  Verdict:**

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
