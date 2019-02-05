import React, { Component } from 'react';
import superagent from 'superagent';

class RegistrationForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            username: '',
            email: '',
            password: ''
        }
        this.onChangeUserName = this.onChangeUserName.bind(this);
        this.onChangeUserEmail = this.onChangeUserEmail.bind(this);
        this.onChangePassword = this.onChangePassword.bind(this);
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

    onChangePassword(event) {
        this.setState({
            password: event.target.value
        });
    }

    onSubmit(event) {
        event.preventDefault();
        const url = 'http://localhost:8000/api/v1/register'
        superagent
            .post(url)
            .send({
                username : this.state.username,
                email: this.state.email,
                password: this.state.password,
            }).then(response => {
                this.props.onRegister({token: response.body.token})
            }).then(token => {

            }).catch(error => {
                console.error(error)
                this.props.onRegister({error:error.toString()})
            });
    }


    render() {
        return (
        <form onSubmit={this.onSubmit}>
            <input name='username' placeholder='user name' value={this.state.username} onChange={this.onChangeUserName} />
            <input name='email' placeholder='user email' value={this.state.email} onChange={this.onChangeUserEmail} />
            <input name='password' type='password' placeholder='password' value={this.state.password} onChange={this.onChangePassword} />
            <button type='submit'>Register</button>
        </form>
        );
    }
}

export default RegistrationForm;
