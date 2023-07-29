# COVID Symptoms Survey Demo
Imagine you're part of the COVID Response team for your university and you're tasked with creating an online survey web app that can record metadata and allow university affiliates to report if they experienced symptoms so that the developers could then try to figure out who else may have been affected. 

I used **Lambda**, **API Gateway**, and **Amplify** to build the main base of the application. You can use whichever service you're comfortable with to store the survey results. In this example, I encoded the data as a bytestream with `UTF-8` settings and created unique `.json` files in **S3** for each first name and last name.

## Step 1 [Amplify]
 - First take `index.html` and then compress into a ZIP folder. 
 - Now, let's set up **Amplify**. Click **Get Started** and then **Deploy without a Git Provider**. 
 - Name your app *whatever* and call your environment `dev`. 
 - Now, **Drag and Drop** your compressed folder. Then, **Save and Deploy**. 
 - Once your code has been deployed on the Amplify web app, it will generate a link. Access it in **Domain Management** and click to preview your website. 

[WARNING: Some parts could be broken]

## Step 2 [S3]
 - Open **S3**. **Create bucket** and name it *whatever* in appropriate region.
 - Keep defaults and **Create bucket**.

## Step 3 [Lambda]
 - As expected, we will plug `lambda.py` into **Lambda**. 
 - **Create Function** and type *whatever* for function name. 
 - Make sure to use `Python 3.8` for runtime. **Create Function** again and you will get "Successfully created the function".
 - Go to **Configuration** and select **Permissions**.
 - Click on link in **Execution role** followed by **Add inline policy**
 - Go to **JSON** tab and copy policy code from `policy.json`
 - **Review Policy** and name it *whatever*
 - **Create Policy**
 - Copy paste the given code into the code area and save. Now, **Select a test event** and then **Configure test events.** 
 - Now, type *whatever* for event name and then copy paste the contents of `test.json`. Finally, **Create** and click the **Test** button. Hopefully, you got "Your response has been collected. Thank you!"
 - Go back to your bucket and check its contents. It should match our expectations of a `jo.json` file. 
 
 [NOTE: For some reason, I couldn't make the policy specific to a **S3** bucket based on ARN. Bonus points if you can figure out how to make the policy ARN-specific. S3 doesn't store duplicates, so a survey filled out by the same person will only update file contents.]

## Step 4 [API Gateway]
 - Go to **API Gateway**. Start with **Create API**. Find **REST API** and **Build**.
 - Choose **REST** protocol and hit **New API**. Make the name *whatever*.
 - Endpoint type should be **Edge optimized** and now **Create API**.
 - Click on **Resources** and then **Create Method**. Select **POST** and checkmark.
 - Select **Lambda function** and name should match *whatever* (Step 2).
 - Click **Save**, **OK**, **Enable CORS**, and finally **Enable CORS and replace existing CORS headers**.
 - Don't worry and click **Yes, replace existing values**.
 - In **Actions**, **Deploy API** and select **[New Stage]** in the drop-down.
 - Make **Stage Name** `dev`
 - Lastly, **Deploy** and make sure to copy URL next to **Invoke URL**.
 - To test, click **Resources** and then **POST**.
 - Now, copy the same **JSON** contents from `test.json` in the lightning bolt.
 - **Test** and ensure response has `Code 200`.
 - Paste **Invoke URL** in line 52 where it says `"YOUR-LINK"`.
 - Save file and upload again to **Amplify** as explained in [Step 1](https://github.com/kathangandhi/cloud/tree/master/COVID#step-1-amplify).

Take a deep breath and try out your website. First cloud project was pretty easy innit?!

Adapted from ["Build a Basic Web Application"](https://aws.amazon.com/getting-started/hands-on/build-web-app-s3-lambda-api-gateway-dynamodb/)