import { ConnectionHandler } from 'relay-runtime';
import {hasValidJwtToken} from "modules/auth/jwtUtils";
import { withRouter } from 'react-router';

const {
  commitMutation,
  graphql,
} = require('react-relay');

const mutation = graphql`
    mutation SignupUserMutation(
    $input: SignupUserMutationInput!
    ) {
        signup(input : $input) {
            authFormPayload{
                    __typename
                    ... on Viewer{
                        tokens{
                            __typename
                            ... on TokensSuccess {
                                token
                            }
                            ... on TokenError {
                                error
                            }
                        }
                    }
                }
        }
    }
`;

function Signup(environment, input: {email: string, password: string}) {
    return fetch('/resources/users', {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            authorization: `Bearer ${hasValidJwtToken().token}`,
            Accept: 'application/json',
            'Content-Type': 'application/json',
        }, // Add authentication and other headers here
        body: JSON.stringify({
            email : input.email,
            password : input.password
        }),
    }).then(
        response => {
            console.log(response);
            if (response.ok) {
                response.json().then(json => {
                    if(json.rc >= 0){
                        window.location.replace('/login');
                    }
                });
            }
        }
    );
}

export default Signup;
