#!/usr/bin/env python
# -*- coding: utf-8 -*-
import picka

print picka.phone_number()
print picka.last_name()
print picka.random_string(8)
print picka.sentence()
print picka.sentence_actual()
assert picka.sentence_actual(86, 93)  == (
"""\
A shock of orange hair a pale face disfigured by a horrible scar which by its contraction has turned up the outer edge of his upper lip a bulldog chin and a pair of very penetrating dark eyes which present a singular contrast to the colour of his hair all mark him out from amid the common crowd of mendicants and so too does his wit for he is ever ready with a reply to any piece of chaff which may be thrown at him by the passers-by."""
)
print picka.timezone_offset()
print picka.language()
print picka.timezone_offset_country()
print picka.screename()
print picka.number(10)
print picka.month()
print picka.month_and_day_and_year()
print picka.special_characters(8)
print picka.postal_code()
print picka.apartment_number()
print picka.gender()
print picka.salutation()
print picka.creditcard('visa')
print picka.male_middle_name()
print picka.city()
print picka.male_full_name_w_middle_initial()
print picka.state_abbreviated()
print picka.street_name()
print picka.initial()
print picka.calling_code_with_country()
print picka.surnames()
print picka.business_title()
print picka.male_middle()
print picka.trash(picka.male_first)
print picka.female_first()
print picka.calling_code()
print picka.male_first()
print picka.timestamp()
print picka.hyphenated_last_name()
print picka.fax_number()
print picka.male_full_name()
print picka.password_alphanumeric(8)
print picka.birthday()
print picka.social_security_number()
print picka.set_of_initials()
print picka.female_middle()
print picka.month_and_day()
print picka.password_alphabetical(8)
print picka.name()
print picka.cvv(3)
print picka.country()
print picka.age()
print picka.city_with_state()
print picka.email()
print picka.female_name()
print picka.street_type()
print picka.suffix()
print picka.url(10)
print picka.password_numerical(10)
print picka.street_address()
print picka.language()
