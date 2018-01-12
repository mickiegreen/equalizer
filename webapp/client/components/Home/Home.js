/* eslint-disable jsx-a11y/href-no-hash */
import React from 'react';
import Page from '../Page/Page';
import Textfield from 'react-mdc-web/lib/Textfield/Textfield';
import Button from 'react-mdc-web/lib/Button';
import Checkbox from 'react-mdc-web/lib/Checkbox';
import LoginUserMutation from '../../modules/auth/mutations/Login';
import SignupUserMutation from '../../modules/auth/mutations/Signup';
import { authenticatedRoute } from '../../modules/auth/utils';
import styles from '../../modules/auth/Auth.scss';
import "../../../node_modules/video-react/styles/scss/video-react.scss";

function isLoginCheck(props) {
    return props.router.match.path === '/login';
}

class Login extends React.Component {
    constructor(props) {
        super(props);
        const initialInput = {
            email: '',
            password: '',
        };

        this.state = {
            input: initialInput,
            isEmailValid: false,
            isPasswordPresent: false,
            errorEmail: false,
            errorPassword: false
        };
    }


    setFormErrors = () => {
        const { isEmailValid, isPasswordPresent } = this.state;
        // If not valid!
        if (!isEmailValid) {
            this.setState({ errorEmail: "Email isn't valid" });
        }
        if (!isPasswordPresent) {
            this.setState({ errorPassword: 'Passwords is blank' });
        }
    };

    handleFieldChange(e) {
        const input = this.state.input;
        const inputName = e.target.id;
        input[inputName] = e.target.value;
        this.setState({ input });
    }

    loginUser = (environment, input) => {
        const mutation = LoginUserMutation(environment, input);
    };
    signupUser = (environment, input) => {
        const mutation = SignupUserMutation(environment, input);
    };

    submitForm = (form) => {
        form.preventDefault();
        const isLogin = isLoginCheck(this.props);
        const { input, isEmailValid, isPasswordPresent } = this.state;
        const { environment } = this.props;

        isLogin ? this.loginUser(environment, input) : this.signupUser(environment, input);
    };

    render() {
        const { input, passwordConfirmation, isEmailValid, isPasswordsMatching } = this.state;
        //const isLogin = isLoginCheck(this.props);

        return (
            <form id={'Login'} onSubmit={this.submitForm} className={styles.form}>
                <div className={styles.formContainer} >
                    <Textfield
                        id='email'
                        className={styles.textFields}
                        onChange={this.handleFieldChange.bind(this)}
                        value={input.email}
                        floatingLabel='Email'
                    />
                    <br />

                    <Textfield
                        id='password'
                        className={styles.textFields}
                        onChange={this.handleFieldChange.bind(this)}
                        value={input.password}
                        floatingLabel='Password'
                        type='password'
                        //error={this.state.errorPassword}
                    />

                    <div style={{ textAlign: 'right' }} >
                        <a href='#' >Forgot password</a>
                        <Button
                            primary
                            className='button_submit-login-form'
                        >Login</Button>
                        <br />
                        <div>
                            <Checkbox
                                label='Remember me'
                                style={{ textAlign: 'right' }}
                            /> <label>Remember Me</label>
                        </div>
                    </div>
                </div>
            </form>
        );
    }
}

class SignUp extends React.Component {
    constructor(props) {
        super(props);
        const initialInput = {
            email: '',
            password: '',
        };

        this.state = {
            input: initialInput,
            isEmailValid: false,
            isPasswordPresent: false,
            errorEmail: false,
            errorPassword: false
        };
    }


    setFormErrors = () => {
        const { isEmailValid, isPasswordPresent } = this.state;
        // If not valid!
        if (!isEmailValid) {
            this.setState({ errorEmail: "Email isn't valid" });
        }
        if (!isPasswordPresent) {
            this.setState({ errorPassword: 'Passwords is blank' });
        }
    };

    handleFieldChange(e) {
        const input = this.state.input;
        const inputName = e.target.id;
        input[inputName] = e.target.value;
        this.setState({ input });
    }

    loginUser = (environment, input) => {
        const mutation = LoginUserMutation(environment, input);
    };
    signupUser = (environment, input) => {
        const mutation = SignupUserMutation(environment, input);
    };

    submitForm = (form) => {
        form.preventDefault();
        const isLogin = isLoginCheck(this.props);
        const { input, isEmailValid, isPasswordPresent } = this.state;
        const { environment } = this.props;

        isLogin ? this.loginUser(environment, input) : this.signupUser(environment, input);
    };

    render() {
        const { input, passwordConfirmation, isEmailValid, isPasswordsMatching } = this.state;
        //const isLogin = isLoginCheck(this.props);

        return (
            <form id={'Sign up'} onSubmit={this.submitForm} className={styles.form}>
                <div className={styles.formContainer} >
                    <Textfield
                        id='email'
                        className={styles.textFields}
                        onChange={this.handleFieldChange.bind(this)}
                        value={input.email}
                        floatingLabel='Email'
                    />
                    <br />

                    <Textfield
                        id='password'
                        className={styles.textFields}
                        onChange={this.handleFieldChange.bind(this)}
                        value={input.password}
                        floatingLabel='Password'
                        type='password'
                        //error={this.state.errorPassword}
                    />
                    <Textfield
                        id='passwordConfirmation'
                        onChange={this.handleFieldChange.bind(this)}
                        value={input.passwordConfirmation}
                        className={styles.textFields}
                        floatingLabel='Password Confirmation'
                        type='password'
                        minLength={8}
                        helptext='Your password must be at least 8 characters'
                        helptextValidation
                    />
                    <div style={{ textAlign: 'right' }} >
                        <Button
                            primary
                            className='button_submit-login-form'
                        >Sign Up</Button>
                        <br />
                    </div>
                </div>
            </form>
        );
    }
}

class Home extends React.Component {
    constructor(props) {
        super(props);
        const initialInput = {
            email: '',
            password: '',
        };
        if (!isLoginCheck(props)) {
            initialInput.passwordConfirmation = '';
        }

        this.state = {
            input: initialInput,
            isEmailValid: false,
            isPasswordPresent: false,
            errorEmail: false,
            errorPassword: false
        };
    }


    setFormErrors = () => {
        const { isEmailValid, isPasswordPresent } = this.state;
        // If not valid!
        if (!isEmailValid) {
            this.setState({ errorEmail: "Email isn't valid" });
        }
        if (!isPasswordPresent) {
            this.setState({ errorPassword: 'Passwords is blank' });
        }
    };

    handleFieldChange(e) {
        const input = this.state.input;
        const inputName = e.target.id;
        input[inputName] = e.target.value;
        this.setState({ input });
    }

    loginUser = (environment, input) => {
        const mutation = LoginUserMutation(environment, input);
    };
    signupUser = (environment, input) => {
        const mutation = SignupUserMutation(environment, input);
    };

    submitForm = (form) => {
        form.preventDefault();
        const isLogin = isLoginCheck(this.props);
        const { input, isEmailValid, isPasswordPresent } = this.state;
        const { environment } = this.props;

        isLogin ? this.loginUser(environment, input) : this.signupUser(environment, input);
    };

    render() {
        const { input, passwordConfirmation, isEmailValid, isPasswordsMatching } = this.state;
        const isLogin = isLoginCheck(this.props);

        return (
            <Page
                heading={'Equalizer'}
                style={{ display: 'flex', justifyContent: 'center' }}
            >
              <Login/>
                <SignUp/>
            </Page>
        );
    }


}


/*class Home extends React.Component {

    render() {
        return (
            <Page heading='' >

            </Page>
        )
            ;
    }


}*/

export default Home;
