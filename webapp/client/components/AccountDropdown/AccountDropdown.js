import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Dropdown, { DropdownTrigger, DropdownContent } from '../../../node_modules/react-simple-dropdown/lib/components/Dropdown.js';
import Link from 'react-router-dom'
import styles from './AccountDropdown.css';
import {getToken, hasValidJwtToken, logoutViewer} from "modules/auth/jwtUtils";

class AccountDropdown extends Component {
    constructor (props) {
        super(props);

        this.handleLinkClick = this.handleLinkClick.bind(this);
        this.handleHistoryClick = this.handleHistoryClick.bind(this);
    }

    handleLinkClick () {
        logoutViewer();
        this.refs.dropdown.hide();
    }

    handleHistoryClick () {
        console.log(this.state);
        console.log(this.props);
        fetch(`/resources/users/history?user_id=${encodeURIComponent(getToken())}`, {
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
                        localStorage.setItem('eqHistoryResults', JSON.stringify(json));
                    }
                }).then(
                    () => {
                        this.refs.searchHistory.click();
                    }
                );
            }
        });
    }

    handleProfileClick () {
        this.refs.dropdown.hide();
    }

    render () {
        const { user } = this.props;

        return (
            <Dropdown className="account-dropdown" ref="dropdown">
                <DropdownTrigger>
                    <img className="account-dropdown__avatar" src={user.avatar_url} />{/*<span className="account-dropdown__name">My Account</span>*/}
                </DropdownTrigger>
                <DropdownContent>
                    <div className="account-dropdown__identity account-dropdown__segment">
                        Signed in as <strong>a member</strong>
                    </div>
                    <ul className="account-dropdown__quick-links account-dropdown__segment">
                        {/*<li className="account-dropdown__link">
                            <a className="account-dropdown__link__anchor" href="/profile" onClick={this.handleLinkClick}>
                                Your profile
                            </a>
                        </li>*/}
                        <li className="account-dropdown__link">
                            <a className="account-dropdown__link__anchor" onClick={this.handleHistoryClick}>
                                Your history
                            </a>
                            <a ref="searchHistory" style={{display: 'none'}} className="account-dropdown__link__anchor" href="#/history">

                            </a>
                        </li>
                        {/*<li className="account-dropdown__link">
                            <a className="account-dropdown__link__anchor" href="#" onClick={this.handleLinkClick}>
                                Explore
                            </a>
                        </li>
                        <li className="account-dropdown__link">
                            <a className="account-dropdown__link__anchor" href="#" onClick={this.handleLinkClick}>
                                Help
                            </a>
                        </li>*/}
                    </ul>
                    <ul className="account-dropdown__management-links account-dropdown__segment">
                        {/*<li className="account-dropdown__link">
                            <a className="account-dropdown__link__anchor" href="#" onClick={this.handleLinkClick}>
                                Settings
                            </a>
                        </li>*/}
                        <li className="account-dropdown__link">
                            <a className="account-dropdown__link__anchor" href="#" onClick={this.handleLinkClick}>
                                Sign out
                            </a>
                        </li>
                    </ul>
                </DropdownContent>
            </Dropdown>
        );
    }
}

AccountDropdown.propTypes = {
    user: PropTypes.object.isRequired
};

export default AccountDropdown;