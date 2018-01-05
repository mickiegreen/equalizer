import React from 'react';
import Page from 'components/Page/Page';
import Link from 'react-router-dom/es/Link';
import Vertical from 'components/Vertical/Vertical';

const Landing = () =>
  <Page heading='Landing' >
    <p>This is the landing page</p>
      <span>
          {/*<Equalizer/>*/}
          <Vertical/>
      </span>
    <Link to='/polls'>Polls</Link>
  </Page>;

export default Landing;
