// ex B

#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;
void main() {
/*gl_FragCoord contém a posição do pixel em relação a viewport/janela,
enquanto que u_resolution contem a resolução da tela.
A variável st recebe a posição do pixel normalizada, de modo que sua
nova faixa de valores passe a ser de 0 a 1, tanto na largura quanto
na altura.
*/
    vec2 st = gl_FragCoord.xy/u_resolution;
    gl_FragColor = vec4(st.y,st.y,st.x,1.0);
}