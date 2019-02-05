import React, { Component } from 'react';
import './App.css';
import Head from './head/head'
import Header from './header/header'
import Landing from './landing/landing'
import Main from './main/main'
import Footer from './footer/footer'



class App extends Component {
  render() {
    return (
      <div className="App">
        <Head />
        <Header />
        <Landing />
        <Main />
        <Footer />
      </div>
    );
  }
}

export default App;
