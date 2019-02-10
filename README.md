<a href='https://coveralls.io/github/Rachelnk/Politico-Forum?branch=master'><img src='https://coveralls.io/repos/github/Rachelnk/Politico-Forum/badge.svg?branch=master' alt='Coverage Status' /></a>
<h1> Politico Forum </h1>
<p>Politico is a web application that enables users to vote for their leaders, individuals interested in running for office can register to run for the specific office.This app allows provides an API that enables admins to create and edit politcal parties offices. The admins and users can also retrieve all political parties and offices as well as a specific political party or office </p>

<h1>Getting Started</h1>
<p> Clone the repository to your local computer or download a zip file and extract. Here's the link to the application https://github.com/Rachelnk/Politico-Forum.git</p>

<h1>Requirements  </h1>
<p>To run the application you will need:
  <li> Python 3.6 . Download it from <a href="">here</a></l1>
  <l1>Flask. Download it from <a href="">here</a></l1>
<l1>Postman. Download it from <a href="">here</a></l1></p>
<p>Once you have installed flask,set up a virtual environment and activate it:<\p> 
  <table><tr><td>
  venv\Scripts\activate 
    </table></tr></td>
<p>Ensure to install the packages in the requirements.txt file</p>
  
<h1>Testing</h1>
<p>Ensure you have installed pytest. To run tests navigate to the tests folder and run pytest -v</p>
 
<h1>EndPoints</h1>
<table>
  <tr>
  <th>Method</th>
   <th>URL</th>
   <th>Funnction</th>
  </tr>
  <tr>
    <td>POST</td>
    <td>/api/v1/parties</td>
    <td>Create a new political party</td>
    </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/parties</td>
    <td>Fetches all the political parties</td>
    </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/parties/<id></td>
    <td>Fetches a specific political party</td>
    </tr>
  <tr>
    <td>DELETE</td>
    <td>/api/v1/parties/<id></td>
    <td>Deletes a political party</td>
    </tr>
  <tr>
    <td>POST</td>
    <td>/api/v1/offices</td>
    <td>Create a new political office</td>
    </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/offices</td>
    <td>Fetches all the political offices</td>
    </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/offices/<id></td>
    <td>Fetches a specific political office</td>
    </tr>
  <h1>License</h1>
  <p> Rachel Kiarie</p>
      
