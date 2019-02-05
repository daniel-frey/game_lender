import React, { Component } from 'react';
import RegistrationForm from '../registration-form/registration-form';


class Landing extends Component {

    constructor(props) {
        super(props)
        this.state = {
            token : ''
        }
        this.handleRegistration = this.handleRegistration.bind(this)
    }

    handleRegistration(response) {
        console.log(response)
        console.log('hello')
        this.setState({token:response.token})
    }

    render() {
        return (
            <div>
                <h1>Registration</h1>
                <RegistrationForm onRegister={this.handleRegistration}/>
                <div>
                <p>{this.state.token}</p>
                </div>
            </div>
        );
    }
}

export default Landing;
