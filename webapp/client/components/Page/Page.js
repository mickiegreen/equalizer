import React from 'react';
import styles from './Page.scss';

const Page = (props: {heading: String, children: Object, style : Object}) =>
  <div className={props.style == undefined ? styles.root : props.style}>
      {props.heading != false ? (
          <h1 className={styles.heading} >
              {props.heading}
              </h1>
          ) : (
              null
          )}
    <div className={styles.body}>
      {props.children}
    </div>
  </div>;

export default Page;
