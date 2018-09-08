# About

The aim of OpenAircraftType is to provide an open-source, adaptable database of aircraft types and varients.

# Where is the data!

The raw data is located in the `src` folder. Compiled versions can be found in the [releases](https://github.com/atoff/OpenAircraftType/releases). However, if you are using the data for a custom application, I highly suggest creating your own compiler tool so you get just the data you want/need.

# Contributing

All contributions are welcome! The goal of this project is to create an up-to-date, reliable database so crowdsourcing is really important in keeping up to date with the ever evolving aircraft market.

Our most important issues are listed in the "Issues" tab. If you are new, you might want to look at one of the issues marked "good first issue" before tackling a larger, more complex issue. If you would like to claim an issue, simply comment on it and we will assign it to you. Try not to work on an issue claimed by someone else, as you might be doing work that has already been done!

### Compiling the database
At the moment, I have written a custom python script for compiling the source data into CSV format. It is included in the `compile` directory, however it isn't pretty...

### File/Folder Structure
The raw data is broken into files and sub-directories to allow for easy committing & PR merging. In theory, it should be very fast to add, edit or delete a aircraft to the database by simply creating a text file in the appropriate location. All you need is a text editor!

The folders are configurated as such:

<ul>
	<li>
    	**MANUFACTURER** Folder - This holds all of the aircraft made by the manufacturer. It contains a aircraft type information file (more on this later)
        <ul>
        <li>**AIRCRAFT TYPE** Folder - This holds all of the information about the type. It contains a '**AIRCRAFT TYPE**.txt' file (more on this later)
          <ul>
          <li>"Varients" Folder - This folder is optional, and contains any varients of the type.It contains a aircraft type information file for each varient</li>
          </ul>
        </li>
        </ul>
    </li>
</ul>

As an example:
<ul>
	<li>
    	AIRBUS
        <ul>
        <li>A320
          <ul>
          <li>
          	Varients
            <ul><li>A320-111.txt</li><li>A320-121.txt</li><li>....txt</li></ul>
          </li>
          <li>A320.txt</li>
          </ul>
        </li>
        <li>manufacturer.txt</li>
        </ul>
    </li>
</ul>

### File Contents

All of the files are in the format of a standard properties file, with the key being the first string
(i.e `MODEL=A320`). If you want to add data that is not covered by the following properties, simply create a suitable, unique name for it and utilize it (making sure to add it to the appropriate section below). Ideally, all properties below are defined for each and every type (and/or varient)!

##### \*\*MANUFACTURER\*\*/manufacturer.txt
This file contains details about the manufacturer. At the moment the following properties are in use in the database.

| Property Key 	| Description   				| Example	|
| --------------|:-----------------------------------------:	|:-------------:|
| NAME      	| The name of the manufacturer 			| Airbus 	|
| COMPANY      	| The corporate name of the manufacturer    	| Airbus SE 	|

##### \*\*MANUFACTURER\*\*/\*\*AIRCRAFT TYPE\*\*/\*\*AIRCRAFT TYPE\*\*.txt *or* \*\*MANUFACTURER\*\*/\*\*AIRCRAFT TYPE\*\*/Varients/\*\*VARIENT\*\*.txt
Here, \*\*AIRCRAFT TYPE\*\* should ideally be the ICAO code of the aircraft type, and \*\*VARIENT\*\* should be the varient model name (e.g A320-111). However, it can in reality be whatever works. This file sets the base properties for the aircraft type (if it is the \*\*AIRCRAFT TYPE\*\*.txt file), or it overwrites/extends the aircraft type base file.

As an example, when you define a varient, say AIRBUS/A320/Varients/A320-111.txt, any properties in this file will overwrite the properties of the AIRBUS/A320/A320.txt file for the varient.

| Property Key 	| Description   							| Example		|
| --------------|:-----------------------------------------:|:-------------:|
| MODEL      	| The name of the model 							| A320 |
| ICAO      	| The ICAO designator of the model, if available    | A320 |
| CLASS      	| The class of the air-vehicle. L=Land Plane,B=Balloon,A=Amphibious,H=Helicopter,G=Gyrocopter,S=Sea Plane,T=Tilt Rotor    									  		| L |
| WAKE      	| Wake Turbulence Category. L=Light,M=Medium,H=Heavy,J=Jumbo,S=Super    | M |
| ENG_TYPE      | Type of engines. P=Piston,J=JET,T=Turboprop/shaft,R=Rocket,E=Electric    | J |
| ENG_NUM      	| Number of engines. Any integer    			| 2 |
| ENG_NAME      | The name/model of the engines    				| IAE V2527E-A5 |
| ENG_MAN      	| The name of the engine manufacturer    		| International Aero Engines |
| ENG_MODEL     | The name of the engine model    				| V2527E-A5 |
| ENG_THRUST    | Thrust per engine in newtons OR Power in horsepower (for prop/turbo props)    				| 118320 |
| LENGTH      	| Length (nose to tail) in meters    			| 37.57 |
| WINGSPAN     	| Wingspan in meters    						| 35.8 |
| TAIL_HEIGHT   | Tail height in meters    						| 11.76 |
| RANGE      	| Range in nautical miles    					| 3300 |
| CEILING      	| Operational ceiling in feet    				| 41000 |
| MAX_SPEED     | Maximum Speed in knots    					| 470 |
| PAX_CAP     	| The maximum passenger capacity    			| 195 |

# Data usage
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
