import React from 'react';
import NavLink from 'react-router-dom/es/NavLink';
import Link from 'react-router'
import Navigation from 'react-mdc-web/lib/Drawer/Navigation';
import Drawer from 'react-mdc-web/lib/Drawer/Drawer';
import DrawerHeader from 'react-mdc-web/lib/Drawer/DrawerHeader';
import DrawerHeaderContent from 'react-mdc-web/lib/Drawer/DrawerHeaderContent';
import DrawerContent from 'react-mdc-web/lib/Drawer/DrawerContent';
import Toolbar from 'react-mdc-web/lib/Toolbar/Toolbar';
import ToolbarSection from 'react-mdc-web/lib/Toolbar/ToolbarSection';
import ToolbarTitle from 'react-mdc-web/lib/Toolbar/ToolbarTitle';
import ToolbarRow from 'react-mdc-web/lib/Toolbar/ToolbarRow';
import Button from 'react-mdc-web/lib/Button/Button';
import Input from 'react-mdc-web/lib/Textfield/Input';
import Icon from 'react-mdc-web/lib/Icon/Icon';
import styles from './Nav.scss';
import {logoutViewer, getUserName, getToken, hasValidJwtToken} from 'modules/auth/jwtUtils';
import { AcountDropdown } from '../AccountDropdown/AccountDropdown';
import AccountDropdown from "components/AccountDropdown/AccountDropdown";
import { HashRouter as Router, Route } from 'react-router-dom';

type NavPropsType = { title: string, isAuthenticated: boolean, isAdmin: boolean }

const iconStyle = {
    height: '35px',
    width: '35px',
    background: '#fff',
    borderRadius: '19px',
    maxWidth: '97%',
    maxHeight: '97%',
    paddingRight: '0px',
    position: 'absolute',
    top: 0
}

const iconStyleSearch = {
    height: '35px',
    width: '35px',
    borderRadius: '19px',
    maxWidth: '97%',
    maxHeight: '97%',
    paddingRight: '0px',
    position: 'absolute',
    top: 0
}

const searchBox = {
    background: 'url("../../../assets/admin/img/search.svg") no-repeat scroll 147px 7px',
    //paddingLeft:'30px',
    margin: 'auto',
    width: '80%',
    backgroundColor: 'rgba(193, 179, 204, 0.72)',
    color : '#fff',
    borderRadius: '15px',
    padding: '8px',
    maxWidth: '200px'
}

const HomeLink = ({ title }: { title: NavPropsType.title }) =>
  <NavLink to='/'>
    <Button >
        {/*<img className="account-dropdown__avatar" src='../../../assets/admin/img/vid-btn-play-icon2.png' />*/}
        <img className="account-dropdown__avatar" style={iconStyle} src='../../../assets/admin/img/PlayButton.png' />
    </Button>
  </NavLink>;

const AdminLink = () =>
  <NavLink to='/admin/' >
    <Button >Admin</Button>
  </NavLink>;

type LinksPropType = { isAuthenticated: NavPropsType.isAuthenticated, isAdmin: NavPropsType.isAdmin };

const headerStyle = {
    color : '#ffffff',
    fontWeight : '650',
    //fontWeight : 300,
    fontFamily: 'GeosansLight',
    position: 'absolute',
    right: '12px'
}

const headerStyle2 = {
    color : '#ffffff',
    fontWeight : '650',
    //fontWeight : 300,
    fontFamily: 'GeosansLight',
    position: 'absolute',
    right: '80px'
}

const user={'name' : 'michael', 'avatar_url' : '../../../assets/admin/img/profile.png'};
const links = (props: LinksPropType) => {
  let NavLinks;
  if (props.isAuthenticated) {
    NavLinks = () =>
      <div>
          {/*<NavLink className='button_login-link' to='/search' >
              <Button >Search Results</Button>
          </NavLink>*/}
          <div style={{display: 'inline-block', paddingTop: '3px', paddingRight: '63px', cursor : 'pointer'}}>
              <AccountDropdown user={user}/>
          </div>
        {props.isAdmin ? <AdminLink /> : null}
      </div>;
  }
  if (!props.isAuthenticated) {
    NavLinks = () =>
      <div style={{minWidth : '140px'}}>
          {/*<NavLink className='button_login-link' to='/home' >
              <Button >Home</Button>
          </NavLink>
          <NavLink className='button_login-link' to='/equalizer' >
              <Button >Equalizer</Button>
          </NavLink>*/}
        <NavLink className='button_signup-link' to='/signup' >
          <Button style={headerStyle2}>Signup</Button>
        </NavLink>
        <NavLink className='button_login-link' to='/login' >
          <Button style={headerStyle}>Login</Button>
        </NavLink>
      </div>;
  }


  return NavLinks;
};

const MobileDrawer = (props: NavPropsType) =>
  <Drawer
    {...props}
  >
    <DrawerHeader>
      <DrawerHeaderContent>
          <HomeLink className='button_home-link' title={props.title} />
      </DrawerHeaderContent>
    </DrawerHeader>
    <DrawerContent>
      <Navigation>
        <props.Links
          isAuthenticated={props.isAuthenticated}
          isAdmin={props.isAdmin}
        />
      </Navigation>
    </DrawerContent>
  </Drawer>;

class Nav extends React.Component {
  constructor(props: Object) {
    super(props);
    this.state = { isOpen: false };
  }

  state: { isOpen: boolean };
  props: NavPropsType;

  _searchText = (e) => {
      if (e.key === 'Enter') {
          console.log(this.state);
          console.log(this.props);
          fetch(`/resources/users/history/search?user_id=${encodeURIComponent(getToken())}&search_string=${encodeURIComponent(this.state.searchContent)}`, {
              method: 'GET',
              credentials: 'same-origin',
              headers: {
                  authorization: `Bearer ${hasValidJwtToken().token}`,
                  Accept: 'application/json',
                  'Content-Type': 'application/json',
              }}).then(response => {

                  console.log(response);
              if (response.ok) {
                  response.json().then(json => {
                      console.log(json);
                      if(json.rc >= 0){
                          localStorage.setItem('eqHistoryResults', JSON.stringify(json));
                      }
                  }).then(
                      () => {
                          this.refs.searchRef.click();
                      }
                  );
              }
          });
      }
  }

  _searchTextChange = (e) => {
      this.setState({
          searchContent : e.target.value
      });
  }

  render() {
    const { isAuthenticated, isAdmin, title, searchContent } = this.props;
    const Links = links({ isAuthenticated, isAdmin, title });

    return (
      <div >
        <Toolbar>
          <ToolbarRow className={styles.toolbarRow} >
            <ToolbarSection align='start' >
              <ToolbarTitle className={styles.title} >
                <HomeLink title={title} />
              </ToolbarTitle>
              <Button
                onClick={() => {
                  this.setState({ isOpen: !this.state.isOpen });
                }}
              >
                <Icon
                  name='menu'
                  className={styles.mobileNavButton}
                />
              </Button>
            </ToolbarSection>
              <ToolbarSection >
                  <ToolbarTitle className={styles.title} >
                  </ToolbarTitle>
                  <div style={{display : getToken() > 0 ? 'block' : 'none' }}>
                      <Input placeholder={"search history"} value={searchContent} style={searchBox} onChange={this._searchTextChange} onKeyPress={this._searchText}/>
                      <a ref='searchRef' style={{display:'none'}} href='#/history'></a>
                  </div>
              </ToolbarSection>
            <ToolbarSection align='end'>
              <Links
                isAuthenticated={isAuthenticated}
                isAdmin={isAdmin}
              />
            </ToolbarSection>
          </ToolbarRow>
        </Toolbar>

        <MobileDrawer
          open={this.state.isOpen}
          onClose={() => {
            this.setState({ isOpen: false });
          }}
          isAuthenticated={isAuthenticated}
          isAdmin={isAdmin}
          Links={Links}
        />

      </div>
    );
  }


}

export default Nav;
