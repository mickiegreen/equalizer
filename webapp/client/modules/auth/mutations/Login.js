import { ConnectionHandler } from 'relay-runtime';
import { setToken, setUserName } from '../jwtUtils';
import {hasValidJwtToken} from "modules/auth/jwtUtils";

const {
  commitMutation,
  graphql,
} = require('react-relay');

const mutation = graphql`
    mutation LoginMutation(
    $input: LoginMutationInput!
    ) {
        login(input : $input) {
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

const tokenName = 'jwtToken';

function Login(environment, input: {email: string, password: string}) {
    return fetch(`/resources/users/login?email=${encodeURIComponent(input.email)}&password=${encodeURIComponent(input.password)}`, {
        method: 'GET',
        credentials: 'same-origin',
        headers: {
            authorization: `Bearer ${hasValidJwtToken().token}`,
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
    }).then(
        response => {
            if (response.ok) {
                response.json().then(json => {
                    //console.log(json);
                    if(json.content.data[0].login > 0){
                        setToken(json.content.data[0].user_id);
                        setUserName(json.content.data[0].user_name);
                    }
                });
            }
        }
    );
  /*commitMutation(
    environment,
    {
      mutation,

      onCompleted: response =>
      {setToken(response.login.authFormPayload.tokens.token); console.log(response)},
      variables: {
        input
      },
        onError: error => console.log(error)
    },
  );*/
}

export default Login;
