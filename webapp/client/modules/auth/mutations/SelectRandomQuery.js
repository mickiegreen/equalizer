import { ConnectionHandler } from 'relay-runtime';
import { setToken, setUserName } from '../jwtUtils';
import {getUserName, hasValidJwtToken, getToken} from "modules/auth/jwtUtils";

/*const {
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
`;*/

const tokenName = 'jwtToken';

function SelectRandomQuery(environment, input: {}) {
    return fetch(`resources/videos/selectrandomquery?user_id=${getToken()}`, {
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
                    console.log(json);

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

export default SelectRandomQuery;