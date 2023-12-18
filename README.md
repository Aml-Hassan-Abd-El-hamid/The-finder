# The Finder
ML-web-based system that can find similar products based on user inputs

That's actually a part of an interview process, I was given 7 hours to do exactly the following:
```
- Build an ML-web-based system that can find similar products based on user inputs, then deploy it. So, we have only one textbox for product input and another one “ie.. label” for model outputs.

You can focus on Arabic-written products only.

Plz, be cautious of similar items such as “هاتف” and “غطاء هاتف”, so each of them shouldn’t appear in the other one’s search.

You can use the attached JSON file “Black Friday” for validation.
```
I have now 5.5 hours left -spent the first 90 minutes planning the work :) - so let's go

I'm done with the initial look of the app, now I have about 4.5 hours, and I'm faced with the winning question, what model should I use to match the product name to one of the products that I have in the validation list of product?<br>
I wasn't provided with training data, computational power or time :) so the best option that I know that I have is a pre-trained model from the amazing HuggingFace 🤗.<br>
Which model should I use in particular? Will that thing is what I'm about to discover, for now, I just know that the main task that this model has to accomplish and the main characteristic that I have in my head currently is that this model has to know how to deal with <b>Arabic language text</b>.
