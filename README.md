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
    - [User Stories](#user-stories)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
      - [**Requirements**](#requirements)
      - [**Expectations**](#expectations)
    - [Design Choices](#design-choices)
      - [**Fonts**](#fonts)
      - [**Colours**](#colours)
    - [Wireframes](#wireframes)
      - [**Site Map**](#site-map)
      - [**Site Layout**](#site-layout)
      - [**User Account Creation**](#user-account-creation)
      - [**Database design**](#database-design)
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

The **goals** of this project are:

### Site Owner Goals ###

### User Stories ###

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

### Wireframes ###

#### **Site Map** ####

Firstly, I have created a site [map](/wireframes/flowcharts/sitemap.png) to identify clear features the site will have when viewed by the visitor, registered user, and admin.

#### **Site Layout** ####

I designed my site moc-ups using [balsamiq wireframes](https://balsamiq.com/). I was focusing on defining the basic layout structure of the app and identifying how displays would change on different screen sizes such as [mobile and larger screens](/wireframes/site-wireframes/about.visitor.png).

You can view all wireframes created for this project [here](/wireframes/site-wireframes).

#### **User Account Creation** ####

To make user account creation logic easier to understand and simplify the management of it, I have created [workflow-chart](/wireframes/flowcharts/account-creation.jpg).

#### **Database design** ####

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
