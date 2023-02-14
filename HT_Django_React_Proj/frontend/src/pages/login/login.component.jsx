// django imports
import { useState } from 'react';

// project imports
import './login.styles.css';
import { API_URL } from '../../constants';

const defaultFormFields = {
    username: '',
    password: ''
};

const Login = () => {

    // pass in default as formFields state
    const [formFields, setFormFields] = useState(defaultFormFields);
    // destructure the values for when needed
    const { username, password } = formFields;

    const resetFormFields = () => {
        setFormFields(defaultFormFields);
    };

    // chain of events for handleChange:
    // - value param means we pass in the empty strings initially
    // - when user types, onChange triggers new value in formField
    // - value becomes the new input from the formField state

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormFields({ ...formFields, [name]: value })
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        fetch(API_URL + 'users/90')
            .then((response) => (response.json()))
            .then((data) => console.log(data))
            .catch((error) => (
                resetFormFields(),
                console.log('Error:', error)
            ));
        
/*
        var response = fetch(API_URL + 'users/', {

            method: 'POST', 
            mode: 'no-cors', 
            body: JSON.stringify(formFields) // body data type must match "Content-Type" header

        });
        if (!response.ok) {
            resetFormFields();
            console.log("couldn't find user")
        }*/

    };

    return (
        <div className='login-form-container'>
            <span>Sign in with your email and password</span>
            <form method='POST' onSubmit={handleSubmit}>
                <label>Username:
                    <input type="text" value={username} onChange={handleChange} name="username"/>
                </label>
                <label>Password:
                    <input type="text" value={password} onChange={handleChange} name="password"/>
                </label>
                <button type='submit'>Sign In</button>
            </form>
        </div>
    );
};

export default Login;

