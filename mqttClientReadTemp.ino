#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>

const char* ssid = "PKT";
const char* password =  "123456a@";
const char* mqttServer = "192.168.0.115";
const int mqttPort = 1883;
const char* mqttUser = "";
const char* mqttPassword = "";
char temp2[50];
double temp1;

// Chân nối với Arduino
#define ONE_WIRE_BUS D5
//Thiết đặt thư viện onewire
OneWire oneWire(ONE_WIRE_BUS);
//Mình dùng thư viện DallasTemperature để đọc cho nhanh
DallasTemperature sensors(&oneWire);

WiFiClient espClient;
PubSubClient client(espClient);
 
void setup() {
 
  Serial.begin(115200);
  sensors.begin();
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
 
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
 
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
 
    if (client.connect("ESP8266Client", mqttUser, mqttPassword )) {
 
      Serial.println("connected");  
 
    } else {
 
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);
 
    }
  }
 
  client.publish("esp/test", "Hello from ESP8266");
  client.subscribe("esp/test");
 
}
 
void callback(char* topic, byte* payload, unsigned int length) {
 
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
 
  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
 
  Serial.println();
  Serial.println("-----------------------");
 
}
 
void loop() {
  sensors.requestTemperatures();  
  Serial.print("Nhiet do");  
  temp1 = sensors.getTempCByIndex(0);
  sprintf(temp2,"%f",temp1);
  Serial.println(temp2); // vì 1 ic nên dùng 0
  client.publish("esp/test", temp2);
  //chờ 1 s rồi đọc để bạn kiệp thấy sự thay đổi
  delay(1000);
  //client.loop();
}

