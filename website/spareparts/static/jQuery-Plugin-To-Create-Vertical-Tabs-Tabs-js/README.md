# jqueryTabs
Simple jQuery Plugin Tabs

#How to use

###Step 1: Link required files
```html
<!-- jQuery library (served from Google) -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<!-- jquery Tabs Javascript file -->
<script src="js/jquery.tabs.min.js"></script>
<!-- jquery Tabs CSS file -->
<link href="css/jquery.tabs.css" rel="stylesheet" />
```

###Step 2: Create HTML markup
```html
<div class="tabs">
	<ul>
	    <li><a href="#one">One</a></li>
	    <li><a href="#two">Two</a></li>
	    <li><a href="#three" class="active">Three</a></li>
	</ul>

  <div id="one" class="tab">
      <h2>1) Lorem ipsum dolor sit amet.</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
  </div>
  <div id="two" class="tab">
      <h2>2) Lorem ipsum dolor sit amet.</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
  </div>
  <div id="three" class="tab">
      <h2>3) Lorem ipsum dolor sit amet.</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
  </div>
  <div style="clear:both"></div>
</div>
```
