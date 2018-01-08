import React from 'react';
//import Page from 'components/Page/Page';
//import Link from 'react-router-dom/es/Link';
//import Vertical from 'components/Vertical/Vertical';
import Profile from 'modules/auth/Profile/Profile';

const viewer = 'michael.green@gmail.com';

const Landing = () =>
    <Profile user={viewer} />
    {/*<Page heading='Landing' >
      <Profile user={viewer} />
      <p>This is the landing page</p>
      <span>
          <Equalizer/>

          <Vertical/>
      </span>
    <Link to='/polls'>Polls</Link>
  </Page>;*/}

export default Landing;
