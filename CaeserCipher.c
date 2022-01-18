#include<stdio.h>

int main(){
    //Code for Encryption
   /*int key,i;
    char b[100],c1;
    printf("Enter message for encryption:");
    scanf("%s", &b);
    printf("Enter key value:");
    scanf("%d",&key);
    for(i=0; b[i]!='\0';i++){
        c1 = b[i];
if(c1 >= 'a' && c1 <= 'z')
{
c1 = c1 + key;
if(c1 > 'z')
{
c1 =c1-'z'+'a'-1;
}
b[i] =c1;
}
else if(c1 >= 'A' && c1 <= 'Z')
{
c1 = c1+key;
if(c1 > 'Z')
{
c1 = c1-'Z'+'A'-1;
}
b[i] = c1;
}
}*/
//Code for Decryption
int i, key;
char a[100], c2;
printf("Enter message to decrypt: ");
scanf("%s",&a);
printf("Enter key value: ");
scanf("%d", &key);
for(i = 0; a[i] != '\0'; ++i)
{
c2 =a[i];
if(c2>= 'a' && c2 <= 'z'){
c2 = c2-key;
if(c2 < 'a')
{
c2 = c2+'z'-'a'+1;
}
a[i] = c2;
}
else if(c2 >= 'A' && c2 <= 'Z')
{
c2 =c2-key;
if(c2 < 'A')
{
c2 =c2+'Z'-'A'+1;
}
a[i] = c2;
}
}
        //printf("Encrypted message is: %s", b);
       printf("Decrypted message is: %s",a);//
        return 0;

}


