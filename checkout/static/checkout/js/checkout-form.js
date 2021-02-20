/**
 * original code idea borrowed from 
 * the fellow student at the CI:
 * https://github.com/irinatu17/Art-of-Tea/blob/master/static/js/checkout_form.js
 * and tailored to my requirements.
 */

$(document).ready(function () {
    // gets the form's fields from the Personal Details and Delivery Info sections (step 1 and step 2)
    const nameRef = document.getElementById('id_full_name');
    const emailRef = document.getElementById('id_email');
    const phoneNumberRef = document.getElementById('id_phone_number');
    const streetAddress1Ref = document.getElementById('id_street_address1');
    const streetAddress2Ref = document.getElementById('id_street_address2');
    const townOrCityRef = document.getElementById('id_town_or_city');
    const countyRef = document.getElementById('id_county');
    const postcodeRef = document.getElementById('id_postcode');
    const countryRef = document.getElementById('id_country');

    // gets the hidden input fields from the last final form (step3) 
    const nameHiddenInputRef = document.getElementById('full_name');
    const emailHiddenInputRef = document.getElementById('email');
    const phoneNumberHiddenInputRef = document.getElementById('phone_number');
    const streetAddress1HiddenInputRef = document.getElementById('street_address1');
    const streetAddress2HiddenInputRef = document.getElementById('street_address2');
    const townOrCityHiddenInputRef = document.getElementById('town_or_city');
    const countyHiddenInputRef = document.getElementById('county');
    const postcodeHiddenInputRef = document.getElementById('postcode');
    const countryHiddenInputRef = document.getElementById('country');
    const saveInfoHiddenInputRef = document.getElementById('save_info');

    // Personal Details form, step 1
    const personalDetailsForm = document.querySelector('#personal-details-form');
    let personalDetailsFormValid;

    // Handles the validation of the first(Personal details) step of the form when "Next" button is clicked
    $('#personal-details-btn').click(function () {

        personalDetailsFormValid = personalDetailsForm.checkValidity();

        if (personalDetailsFormValid) {
            //if valid,  gets the values of the first fieldset
            let name = nameRef.value;
            let email = emailRef.value;
            let phoneNumber = phoneNumberRef.value;
            // stores those values and add them to hidden input fields in the final form to submit
            nameHiddenInputRef.value = name;
            emailHiddenInputRef.value = email;
            phoneNumberHiddenInputRef.value = phoneNumber;

            // sends the user's input to display in a Form Summary table before the final form is submitted
            $('#full-name-table').text(name);
            $('#email-table').text(email);
            $('#phone-number-table').text(phoneNumber);

            // activates the next tab on click, when form-set is valid 
            $('.nav-tabs .active').parent().next('li').removeClass('disabled');
            $('.nav-tabs .active').parent().next('li').find('a[data-toggle]').attr('data-toggle', 'tab');
            $('.nav-tabs .active').parent().next('li').find('a').trigger('click');
        }
    });

    // Delivery Info form, step 2
    const deliveryInfoForm = document.querySelector('#delivery-info-form');
    let deliveryInfoValid;

    // handles the validation of the second(Delivery Info) step of the form when "Next" button is clicked
    $('#delivery-info-btn').click(function () {
        deliveryInfoValid = deliveryInfoForm.checkValidity();

        if (deliveryInfoValid) {
            //if valid,  gets the values of the second fieldset
            let streetAddress1 = streetAddress1Ref.value;
            let streetAddress2 = streetAddress2Ref.value;
            let townOrCity = townOrCityRef.value;
            let county = countyRef.value;
            let postcode = postcodeRef.value;
            let country = countryRef.value;
            // stores those values and add them to hidden input fields in the final form to submit
            streetAddress1HiddenInputRef.value = streetAddress1;
            streetAddress2HiddenInputRef.value = streetAddress2;
            townOrCityHiddenInputRef.value = townOrCity;
            countyHiddenInputRef.value = county;
            postcodeHiddenInputRef.value = postcode;
            countryHiddenInputRef.value = country;

            // sends the user's input to display in a Form Summary table before the final form is submitted
            $('#street-address1-table').text(streetAddress1);
            $('#street-address2-table').text(streetAddress2);
            $('#town-or-city-table').text(townOrCity);
            $('#county-table').text(county);
            $('#postcode-table').text(postcode);
            $('#country-table').text(country);

            // gets save-info value(true or false) if a user is authenticated(otherwise this field is hidden)
            let saveInfoExist = document.getElementById('id-save-info');
            if (saveInfoExist) {
                let saveInfo = document.getElementById('id-save-info').checked;
                saveInfoHiddenInputRef.value = saveInfo;
            }

            // activates the next tab on click, when the form-set is valid
            $('.nav-tabs .active').parent().next('li').removeClass('disabled');
            $('.nav-tabs .active').parent().next('li').find('a[data-toggle]').attr('data-toggle', 'tab');
            $('.nav-tabs .active').parent().next('li').find('a').trigger('click');
        }
    });

    // back button 
    $('.btnBack').click(function () {
        $('.nav-tabs .active').parent().prev('li').find('a').trigger('click');
    });
});