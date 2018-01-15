import React from 'react';
import NavLink from 'react-router-dom/es/NavLink';
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
import {logoutViewer, getUserName, getToken} from 'modules/auth/jwtUtils';
import { AcountDropdown } from '../AccountDropdown/AccountDropdown';
import AccountDropdown from "components/AccountDropdown/AccountDropdown";

type NavPropsType = { title: string, isAuthenticated: boolean, isAdmin: boolean }

const iconStyle = {
    height: '35px',
    width: '35px',
    background: '#fff',
    borderRadius: '19px',
    maxWidth: '97%',
    maxHeight: '97%',
    paddingRight: '0px',
}

const iconStyleSearch = {
    height: '35px',
    width: '35px',
    borderRadius: '19px',
    maxWidth: '97%',
    maxHeight: '97%',
    paddingRight: '0px',
}

const HomeLink = ({ title }: { title: NavPropsType.title }) =>
  <NavLink to='/' >
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
    fontFamily: 'GeosansLight'
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
          <div style={{display: 'inline-block', paddingTop: '9px', paddingRight: '29px', cursor : 'pointer'}}>
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
          <Button style={headerStyle}>Signup</Button>
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

  render() {
    const { isAuthenticated, isAdmin, title } = this.props;
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
                      <Input style={{ margin: 'auto', width: '66%', backgroundColor: 'rgb(90, 88, 88)', color : '#fff', borderRadius: '21px', padding: '8px'}}/>
                      <Button
                          onClick={() => {
                              this.setState({ search: true });
                          }}
                      >
                          <img className="account-dropdown__avatar" style={iconStyleSearch} src='../../../assets/admin/img/search.svg' />
                      </Button>
                  </div>
              </ToolbarSection>
            <ToolbarSection align='end'> {/*style={{position: 'absolute', right: '10px'}}*/}
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
