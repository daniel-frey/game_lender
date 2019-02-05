import React from 'react';

const Header = () => {
    return (
        <header>
  <div className="top container">
    <div className="row">
      <div className="col-md-12">
        <img className="toplogo" src="images/logo.png"/>
      </div>
    </div>
  </div>

  <div id="nav-wrapper">
    <div id="nav" className="navbar navbar-default navbar-inner container">
        <div className="row">
          <div className="col-md-10 col-md-offset-1">
            <div className="navbar-header">
               <span className="icon-bar"></span>
               <span className="icon-bar"></span>
               <span className="icon-bar"></span>
            </div>

            <div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
              <ul className="nav navbar-nav">
                <li className="dropdown">
                  <a href="#" className="dropdown-toggle" data-toggle="dropdown">Categories <span className="fa fa-arrow-down"></span></a>
                  <ul className="dropdown-menu" role="menu">
                    <li><a href="#"><span className="glyphicon glyphicon-asterisk"></span> ITEM</a></li>
                    <li className="divider"></li>
                    <li><a href="#"><span className="glyphicon glyphicon-asterisk"></span> Item1</a></li>
                    <li><a href="#"><span className="glyphicon glyphicon-asterisk"></span> Item2</a></li>
                    <li><a href="#"><span className="glyphicon glyphicon-asterisk"></span> Item3</a></li>
                  </ul>
                </li>
              </ul>
              
              <ul className="nav navbar-nav navbar-right">
                <li><a href="index.html"><span className="fa fa-home"></span> Home</a></li>
                <li><a href="contact.html"><span className="fa fa-envelope"></span> Contact</a></li>
              </ul>
            </div>
		
          </div>
        </div>
    </div> 
  </div>
</header>
    );
};

export default Header;