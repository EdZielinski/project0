#   Project0
*	This website consists of four pagess.  There are the home, services, testimonials and FAQ pages.  It is possible to get from any page on the website to any other page by following the hyperlinks.
*	Website must include at least one list (ordered or unordered), at least one table, and at least one image.
o	There are five images, and the img selector centers the images on the Testimonial page.
o	Two unordered lists on the main page
o	One table on the FAQ page
	This table has its style defined on the FAQ page.
•	Website must have at least one stylesheet file.
o	There is one stylesheet file named style_main.css that drives most of the formatting for the entire website.
•	Stylesheet(s) must use at least five different CSS properties, and at least five different types of CSS selectors.  You must use the #id selector at least once and the .class selector at least once.
	At least five different CSS properties are used.
	color
	background-color
	padding
	border
	display
	margin-left
	margin-right
	text-align
	height
	background
	font size
	width
	position
	z-index
	top
	overflow-x
	text-decoration
o	The #id selector is used at least once
	#grad1 selector to define the gradient in the header
o	The  .class selector is used at least once
	The ‘main’ class is used for the main definition of the webpage to allow for the sidenav bar to float up and down the left side of each page
o	Other class selectors
	The ‘sidenav’ class defines the properties and methods of the side nav bar.
	The ‘ctr’ div is used to define the table class on the FAQ page
	The ‘cntr’ class is used to define the centering class for images on the Testimonial page
	The ‘container’ class from Bootstrap displays the Services Provided on the ServicesProvided page, along with the ‘row’ and ‘column’ classes.
o	There is at least one mobile responsive @media query
	The sidenav bar defined in the separate css stylesheet uses an @media query to keep the sidenav bar displayed in the screen while the user scrolls up and down on the page.
	The @media print is also used on the Testimonial Page to not display the Customer Comments when the user wants to print the web-page
o	Bootstrap 4 is used on the ServicesProvided page
	This page has 4 columns for layout purposes to use Bootstrap’s Grid Model to display Services Provided
	Another component of Bootstrap 4 was to display the datalist.  This has auto search by letter to make it easier to search a list while on a mobile device.
o	Use of SCSS variables in the style_main.css file
	The h4 and h6 colors used the sourceMapping URL to nest h4 and h6 colors.
	The sideNAV_FLOAT used the sourceMapping URL to use inheritance for the hover property in the sidenav class in the style_main.css file.
o	Additional features
	On the Services Provided page, yellow highlighted boxes are for text entries.  The grey highlighted box is for an e-mail entry, and there is a place to add files also.  The drop down list is auto search by letter.
