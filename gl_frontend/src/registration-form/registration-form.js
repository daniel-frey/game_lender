import React, { Component } from 'react';
import superagent from 'superagent';

class RegistrationForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            username: '',
            email: '',
            password1: '',
            password2: ''
        }
        this.onChangeUserName = this.onChangeUserName.bind(this);
        this.onChangeUserEmail = this.onChangeUserEmail.bind(this);
        this.onChangePassword1 = this.onChangePassword1.bind(this);
        this.onChangePassword2 = this.onChangePassword2.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    }

    onChangeUserName(event) {
        this.setState({
            username: event.target.value
        });
    }

    onChangeUserEmail(event) {
        this.setState({
            email: event.target.value
        });
    }

    onChangePassword1(event) {
        this.setState({
            password1: event.target.value
        });
    }

    onChangePassword2(event) {
        this.setState({
            password2: event.target.value
        });
    }

    onSubmit(event) {
        event.preventDefault();
        const url = 'http://localhost:8000/auth/v1/registration/'
        superagent
            .post(url).set('Content-Type', 'application/json')
            .send(this.state)
            .then(response => {
                this.props.onRegister({token: response.body.token})
                console.log(response.body);
            }).then(token => {

            }).catch(error => {
                console.error(error)
                this.props.onRegister({error:error.toString()})
        });
    }

    render() {
        return (
        <form onSubmit={this.onSubmit} class="container">
            <input name='username' placeholder='user name' value={this.state.username} onChange={this.onChangeUserName} />
            <input name='email' placeholder='user email' value={this.state.email} onChange={this.onChangeUserEmail} />
            <input name='password' type='password' placeholder='password' value={this.state.password1} onChange={this.onChangePassword1} />
            <input name='verify-password' type='password' placeholder='verify password' value={this.state.password2} onChange={this.onChangePassword2} />
            <button type='submit' class="btn btn-skin">Register</button>
        </form>
        );
    }
}

export default RegistrationForm;
