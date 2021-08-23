<h2>Content Based Image Retreival System</h2>
<h5>Brief:</h5>
<p>It is basically a simple image search engine, which retreives the similar images from the database
on the basis of comparison between their features.Two different methods have been implemented for this purpose--</p>
<p><b>1.Color Histogram</b> method which compares images on the basis of color similarity between them.Color histogram of 8X12X3 bins is used.As a result each image is represented as 288 floating point numbers,further each image has been divided into five segments for localization.So per image we are storing 5 X 288 numbers.These features are then stored in a CSV file for future matching</p>
<p><b>2.ORB feature detection</b> algorithm which matches on the basis of distance between the keypoints.
The ORB algo returns the keypoints and their descriptors for the image provided.These descriptors are stored in the Mysql database as BLOB's.For matching the descriptors for query image and database images are passed to the function one by one.The function returns the distance matrix.Here i have taken the sum of these distances and stored them in a dictionary(per image).Then the top results are displayed.</p>
<h4>Technologies used:</h4>
<ul class="list-style-type:disc">
	<li>Python 2.7</li>
	<li>OpenCv 3.0 for Image processing</li>
	<li>Numpy for mathematical calculations</li>
	<li>Tkinter for GUI</li>
	<li>Mysql Database</li>
	<li>Other python libraries like Mysqldb,Pickle etc</li>
</ul>
<h4>Usage:</h4>
<ul class="list-style-type:disc">
	<li>Install all the requirements as stated above.Project is in my_contrib folder.</li>
	<li>change the paths and database table name,fields in the files index.py,search.py,save_data.py and 
	search_img.py</li>
	<li>Run the main.py script</li>
	<li>Select the method from dropdown provided</li>
	<li>Enter the path of CSV file for indexing in case of color histogram and folder path as required,
	it can be made dynamic as required,i have,however fixed the paths.</li>
	<li>finally enter one of the image in the dataset as query image(full name)</li>
	<li>click on search to find the similar images</li>
</ul>
<h4>Results:</h4>
<p>For images which have been either cropped,rotated or blurred , but are similar on the basis of their content
,ORB gives good result.But for images which are similar in color content,Color Histogram is good.It depends upon the scenerio.</p>
<h4>Bugs:</h4>
<p>1. There is some problem with tkinter and opencv imshow, as after displaying the results the tkinter window has to be forced close every time</p>
<p>2. The accuracy of ORB needs to be improved</p>
<h5>For further queries and improvement drop a mail on farhan0581@gmail.com</h5>