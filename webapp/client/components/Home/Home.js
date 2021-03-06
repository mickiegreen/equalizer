/* eslint-disable jsx-a11y/href-no-hash */
import React from 'react';
import Page from '../Page/Page';
import Textfield from 'react-mdc-web/lib/Textfield/Textfield';
import Button from 'react-mdc-web/lib/Button';
import Checkbox from 'react-mdc-web/lib/Checkbox';
import LoginUserMutation from '../../modules/auth/mutations/Login';
import SignupUserMutation from '../../modules/auth/mutations/Signup';
import { SelectRandomQuery } from '../../modules/auth/mutations/SelectRandomQuery';
import "../../../node_modules/video-react/styles/scss/video-react.scss";
import styles from './Home.scss';
import Vertical from '../Vertical/Vertical';
import { HashRouter as Router, Route } from 'react-router-dom';
import {hasValidJwtToken} from "modules/auth/jwtUtils";
import SearchResults from "components/SearchResults/SearchResults";
import History from "components/History/History";
import fontStyles from '../../../static/admin/fonts/font.css';

function isLoginCheck(props) {
    console.log("isLogin :: " + props.router.match.path === '/login');
    return props.router.match.path === '/login';
}

const formButton = {
    border: '1px solid #ffffff',
    borderRadius: '6px',
    color: '#fff',
    fontFamily: 'GeosansLight',
    fontWeight: 'bolder',
    width: '140px',
    backgroundColor: 'rgba(0,0,0,.37)',
}

const EQStyle = {
    width: '100%',
    height: '30px',
    maxWidth: '483px',
    margin: 'auto',
}

const EQBtnStyleLeft = {
    float: 'left',
    borderColor: '#fff',
    border: '2px solid #fff',
    borderRadius: '6px',
    width: '48%',
    maxWidth: '150px'
}

const EQBtnStyleRight = {
    float: 'right',
    borderColor: '#fff',
    border: '2px solid #fff',
    borderRadius: '6px',
    width: '48%',
    maxWidth: '150px',
    backgroundColor: '#3b0e5478'
}

const AFont = {
    fontWeight:'650',
    color: '#fff',
    textAlign: 'center',
    margin: 'auto',
    width: '100%',
    fontFamily: 'GeosansLight',
    letterSpacing: '2px',
    //paddingLeft: '23px'
    backgroundColor: '#3b0e5478'
}

const ButtonFont = {
    fontWeight:'650',
    color: '#fff',
    //paddingLeft: '44px'
    textAlign: 'center',
    margin: 'auto',
    width: '100%',
    fontFamily: 'GeosansLight',
    letterSpacing: '2px'
}

const welcomeStyle = {
    color : 'white',
    fontWeight : 300,
    fontFamily: 'GeosansLight',
    margin : 'auto',
    textAlign : 'center'
}

function getToken() {
    return localStorage.getItem('jwtToken') == null ? -1 : localStorage.getItem('jwtToken');
}

class Main extends React.Component {
    constructor(props) {
        super(props);

        const initialInput = {
            email: '',
            password: '',
        };

        this.state = {
            custom: false,
            random: true,
            input: initialInput,
            isEmailValid: false,
            isPasswordPresent: false,
            errorEmail: false,
            errorPassword: false,
            showLoginForm: false,
            showSignUpForm: false
        };
    }

    checkLogin = () => {

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

    customQuery = () => {
        console.log("customQuery");
        this.setState({custom: !this.state.custom});
        console.log(this.state.custom);
    }

    randomQuery = () => {
        console.log("randomQuery");
        fetch(`/resources/videos/random?user_id=${encodeURIComponent(getToken())}`, {
            method: 'GET',
            credentials: 'same-origin',
            headers: {
                authorization: `Bearer ${hasValidJwtToken().token}`,
                Accept: 'application/json',
                'Content-Type': 'application/json',
            }}).then(response => {
            if (response.ok) {
                response.json().then(json => {
                    console.log(json);
                    if(json.rc >= 0){
                        localStorage.setItem('eqSearchResults', JSON.stringify(json));
                    }
                }).then(
                    () => {
                        this.props.history.push({
                            pathname : '/search',
                            props: this.props
                        });
                    }
                );
            }
        });


        /*fetch(`/resources/videos/randomQuery?user_id=${encodeURIComponent(getToken())}`, {
            method: 'GET',
            credentials: 'same-origin',
            headers: {
                authorization: `Bearer ${hasValidJwtToken().token}`,
                Accept: 'application/json',
                'Content-Type': 'application/json',
            }}).then(response => {
                console.log(response);
                history.push({
                    pathname : '/search',
                    data: response.json()
                });
            });*/
    }

    showLogin = () => {
        console.log("showLogin");
        this.setState({showLoginForm: !this.state.showLoginForm, showSignUpForm : false});
    }

    showSignUp = () => {
        console.log("showSignUp");
        this.setState({showSignUpForm: !this.state.showSignUpForm, showLoginForm : false});
    }

    handleFieldChange(e) {
        const input = this.state.input;
        const inputName = e.target.id;
        input[inputName] = e.target.value;
        this.setState({ input });
    }

    loginUser = (environment, input) => {
        LoginUserMutation(environment, input).then( response => {
                if (getToken() > 0) {
                    this.setState({showLoginForm: false, showSignUpForm: false});
                }
            }
        );
    };
    signupUser = (environment, input) => {
        const mutation = SignupUserMutation(environment, input);
    };

    submitForm = (form) => {
        form.preventDefault();
        //const isLogin = isLoginCheck(this.props);
        const { input, isEmailValid, isPasswordPresent } = this.state;
        const { environment } = this.props;

        this.state.showLoginForm ? this.loginUser(environment, input) : this.signupUser(environment, input);
    };

    render() {
        const { input, passwordConfirmation, isEmailValid, isPasswordsMatching } = this.state;
        const isLogin = getToken() === null || getToken() === undefined ? false : (getToken() > 0 ? true : false);
        const { custom, random } = this.state;

        return(
            <Page heading={false}>
                <div style={{padding:'none'}}>
                    <br/>
                    <h1 style={welcomeStyle}>Welcome to Equalizer</h1>
                    <h2 style={welcomeStyle}>Customize your music search and build your playlist</h2>
                </div><br/><br/>
                <div style={EQStyle}>
                    <div style={EQBtnStyleLeft}>
                        <Button
                            primary
                            className='mdc-button mdc-button--primary button_submit-login-form'
                            display={'inline-block'}
                            onClick={!isLogin ? this.showSignUp : this.randomQuery}
                            style={AFont}
                        >{isLogin ? 'I Feel Lucky' : 'Sign Up'}
                        </Button>
                    </div>
                    <div style={EQBtnStyleRight}>
                        <Button
                            primary
                            className='button_submit-login-form'
                            onClick={!isLogin ? this.showLogin : this.customQuery}
                            display={'inline-block'}
                            style={ButtonFont}

                        >{isLogin ? 'Custom' : 'Login'} </Button>
                    </div>
                </div><br/><br/>
                <div style={{display : !this.state.custom ? 'none' : 'block'}} >
                    <Vertical history={this.props.history}/>
                </div>
                <div className={styles.formStyle} style={{display : !this.state.showLoginForm && !this.state.showSignUpForm ? 'none' : 'block'}}>
                    <form
                        id={this.state.showLoginForm ? 'Login' : 'Sign up'}
                        onSubmit={this.submitForm}
                        className={styles.form}
                    >

                        <div className={styles.formContainer} >
                            <div style={{display: 'block', height:'35px'}}>
                                <h1 className={styles.formHeader}>{this.state.showLoginForm ? 'Login' : ' Sign up'}</h1>
                            </div>
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
                            />
                            {!this.state.showLoginForm ?
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
                                : null}

                            <div style={{ textAlign: 'right' }} >

                                {/*<a href='#' >Forgot password</a>*/}
                                <Button
                                    primary
                                    className='button_submit-login-form'
                                    style={formButton}
                                >{this.state.showLoginForm ? 'Login' : 'Sign up'}</Button>
                                { isLogin ?
                                    <div>
                                        <Checkbox
                                            label='Remember me'
                                            style={{ textAlign: 'right', border: '2px solid #ffffff' }}
                                        /> <label>Remember Me</label>
                                    </div> : null }
                            </div>
                        </div>
                    </form>
                </div>
            </Page>
        );

    }
}



class Home extends React.Component {
    constructor(props) {
        super(props);
        console.log(this.props.history);
        const initialInput = {
            email: '',
            password: '',
        };

        this.state = {
            custom: false,
            random: true,
            input: initialInput,
            isEmailValid: false,
            isPasswordPresent: false,
            errorEmail: false,
            errorPassword: false,
            showLoginForm: false,
            showSignUpForm: false
        };
    }

    render() {
        return(
            <Page heading={false}>
                <Router history={this.props.history}>
                    <div>
                        <Route exact path="/" component={Main} />
                        <Route path="/search" component={SearchResults} />
                        <Route path="/history" component={History} />
                    </div>
                </Router>
            </Page>
        );
    }
}



export default Home;
