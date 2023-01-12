
import "./App.css";
import React, { Component } from "react";
import axios from 'axios';
import { BrowserRouter as  Link } from "react-router-dom";

class Menu extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: "", list: [],table:[0,1,2,3] };
  }

  

  render() {
    return (
      <div>
       <img style={{width:"80px"}} src="menu.png" alt="my imag"  />
        </div>
    );
  }
}


export default Menu;
