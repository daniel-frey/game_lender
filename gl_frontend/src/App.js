import React, { Component } from 'react';
import './App.css';
import './css/style.css'
import './css/bootstrap.min.css'
import Head from './head/head'
import Header from './header/header'
import Landing from './landing/landing'
import Main from './main/main'
import Footer from './footer/footer'
import './fonts/glyphicons-halflings-regular.eot'
import './font-awesome-4.4.0/css/font-awesome.min.css'


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
